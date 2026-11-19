# detections

Detection rules for AWS and Kubernetes, written in [Sigma](https://sigmahq.io) and Falco, with test events
for each rule and a CI job that runs them on every change.

Rules were built against a multi-account AWS Organization (CloudTrail org trail, GuardDuty, Athena) and
checked against real attack techniques run with [Stratus Red Team](https://github.com/DataDog/stratus-red-team).

## Rules

| Rule | ATT&CK | Level |
|---|---|---|
| [CloudTrail logging tampered](rules/aws/aws_cloudtrail_logging_tampered.yml) | T1562.008 | high |
| [Console login without MFA](rules/aws/aws_console_login_without_mfa.yml) | T1078.004 | medium |
| [Brute force then successful login](rules/aws/aws_console_brute_force_then_success.yml) | T1110 | high |
| [IAM policy attached to self](rules/aws/aws_iam_policy_attached_to_self.yml) | T1098 | high |
| [AdministratorAccess attached](rules/aws/aws_iam_admin_policy_attached.yml) | T1098 | high |
| [Backdoor admin user](rules/aws/aws_iam_backdoor_admin_user.yml) | T1136.003 | critical |
| [Log bucket short expiration](rules/aws/aws_s3_log_bucket_short_expiration.yml) | T1070 | medium |
| [Shell in application container](rules/falco/pygoat_shell_in_container.yaml) (Falco) | T1059 | warning |
| [Access key used from a new network](hunts/aws_access_key_new_source.md) (SQL hunt) | T1078.004 | medium |

## Runbooks

Each of the main rules links to a runbook in [`runbooks/`](runbooks/): what the alert means, how to triage it,
when it's benign, when to escalate, and how to contain it.

## Tests

Each tested rule has two events in `tests/fixtures/<rule>/`:

- `positive.json`: the attack. The rule must fire.
- `negative.json`: a harmless event that looks close. The rule must stay quiet.

CI runs every pair through [Zircolite](https://github.com/wagga40/Zircolite). A rule that misses its attack or
fires on its benign event fails the build.

```
python tests/run.py /path/to/zircolite
```

All account IDs, names and IPs in the fixtures are placeholders.
