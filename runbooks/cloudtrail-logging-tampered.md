# CloudTrail logging tampered

**Rule:** [aws_cloudtrail_logging_tampered](../rules/aws/aws_cloudtrail_logging_tampered.yml) · **Severity:** high · **ATT&CK:** T1562.008

## What it means
Someone stopped, deleted or changed a trail. Attackers do this first so the rest of their activity isn't recorded.

## Triage
1. Who made the call? Check `userIdentity.arn` and `sourceIPAddress`.
2. Is there an approved change for this trail right now? Ask the change owner, not the caller.
3. Is the trail still logging? `aws cloudtrail get-trail-status --name <trail>`
4. What else did the same identity do in the last hour? Run the query below.

## Benign if
A planned change with a ticket, made by the pipeline role, and the trail is logging again.

## Escalate if
No ticket, a human or unknown identity, a new IP, or other unusual calls around it. Declare SEV1: you may be
blind from this point on.

## Contain
1. Restart logging: `aws cloudtrail start-logging --name <trail>`
2. Deactivate the caller's keys and attach a deny-all policy to the identity.
3. Remember the org trail and the SCP that blocks this. Check why the SCP didn't stop it.

## Evidence
```sql
SELECT eventtime, eventname, eventsource, sourceipaddress, errorcode
FROM cloudtrail_org
WHERE useridentity.arn = '<arn>'
  AND from_iso8601_timestamp(eventtime) > current_timestamp - interval '1' hour
ORDER BY eventtime;
```
