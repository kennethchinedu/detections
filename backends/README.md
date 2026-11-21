# Converting the rules to other SIEMs

The rules in [`rules/`](../rules/) are Sigma. `sigma-cli` turns them into a query for a named SIEM (a **backend**).
A **pipeline** maps field and table names to that SIEM's schema. A query can be valid and still match nothing if the
pipeline is missing or wrong.

Converted on 2026-11-21 in AWS CloudShell: `sigma-cli 4.0.1`, `pySigma 2.1.0`, `pysigma-backend-splunk 3.0.1`.

## Splunk (SPL)

```
sigma convert -t splunk --without-pipeline -s rules/aws/ -o backends/splunk/all-rules.spl
```

`--without-pipeline` keeps CloudTrail's own field names, which is how Splunk's AWS add-on stores them.
`-s` skips rules that can't be converted instead of stopping.

| Rule | Result |
|---|---|
| CloudTrail logging tampered | converted |
| Console login without MFA | converted |
| Brute force then success (temporal_ordered) | converted, with a caveat (below) |
| AdministratorAccess attached | converted |
| Backdoor admin user (temporal, 3 rules) | converted only when the whole folder is loaded; with a caveat |
| Log bucket short expiration | converted |
| IAM policy attached to self | **not converted**: "ORing FieldRef matching is not yet supported by Splunk backend" |

Example, CloudTrail logging tampered:
```
eventSource="cloudtrail.amazonaws.com" (eventName IN ("StopLogging", "DeleteTrail", "UpdateTrail", "PutEventSelectors")) NOT userIdentity.arn="*AWSServiceRoleFor*"
```

Backdoor admin user:
```
| multisearch
[ search eventSource="iam.amazonaws.com" eventName="CreateUser" | eval event_type="aws_iam_user_created" ]
[ search eventSource="iam.amazonaws.com" eventName="CreateAccessKey" | eval event_type="aws_iam_access_key_created" ]
[ search eventSource="iam.amazonaws.com" (eventName IN ("AttachUserPolicy", "AttachRolePolicy", "AttachGroupPolicy")) requestParameters.policyArn="*/AdministratorAccess" NOT userIdentity.arn="*AWSServiceRoleFor*" | eval event_type="aws_iam_admin_policy_attached" ]
| bin _time span=10m
| stats dc(event_type) as event_type_count by _time userIdentity.arn
| search event_type_count >= 3
```

## Microsoft Sentinel (KQL)

`pySigma-backend-kusto 0.4.5` doesn't work with `pySigma 2.x`: installing it made every `sigma` command fail
(`cannot import name 'SigmaTransformationError'`). In a separate virtual environment with `sigma-cli 1.0.6` it
loaded, then failed on conversion (`'str' object is not callable`).

Its pipelines (`microsoft_xdr`, `microsoft_365_defender`, `azure_monitor`, `sentinel_asim`) cover Windows and Azure
tables. None maps CloudTrail fields to Sentinel's `AWSCloudTrail` table (`EventName`, `EventSource`,
`UserIdentityArn`), so KQL for these rules is written by hand or needs a custom pipeline.

## Datadog and Athena

- Datadog backend: state "testing", marked not compatible with `sigma-cli 4.0.1`. Not installed.
- Athena: no backend. The SQL versions are written by hand (see [`hunts/`](../hunts/)).

## What to watch for

1. **A missing backend.** Athena has none and Datadog's lags behind, so those versions are written by hand.
2. **Version breakage.** One incompatible plugin breaks the whole CLI. Install each backend in its own virtual
   environment and pin the versions in CI.
3. **Field mapping.** Without the right pipeline the query runs but matches nothing.
4. **Unsupported features.** `fieldref` joined by OR doesn't convert to Splunk. Fix: split
   `aws_iam_policy_attached_to_self` into a user rule and a role rule.
5. **Correlation references.** A correlation rule only converts when the rules it names are loaded with it. Convert
   the folder, not the file.
6. **Changed meaning.** Sigma's `timespan: 10m` means any 10 minutes. The Splunk output uses fixed 10-minute buckets
   (`bin _time span=10m`), so CreateUser 10:08, CreateAccessKey 10:09, AttachUserPolicy 10:11 is missed: no bucket
   holds all three. Brute force has the same gap. Fix in Splunk with a sliding window (`streamstats time_window=10m`
   or `transaction maxspan=10m`), tested on real events.
7. **Converted isn't tested.** Each output still has to fire on a real event in the SIEM.
