# Access key used from a new network

**ATT&CK:** T1078.004 · **Level:** medium · **Runs on:** Athena over an organization CloudTrail

"New" means never seen before, which needs a baseline of past activity. Sigma matches events against fixed
values and has no memory, so this lives as a scheduled SQL hunt instead of a rule.

CloudTrail records the source IP, not the network owner (ASN). Without enrichment, the query uses the first
two octets as a rough stand-in. With ASN enrichment (Datadog, Sentinel), use the ASN.

```sql
WITH baseline AS (
  SELECT DISTINCT
    useridentity.accesskeyid AS key_id,
    split_part(sourceipaddress, '.', 1) || '.' || split_part(sourceipaddress, '.', 2) AS net
  FROM cloudtrail_org
  WHERE timestamp >= '2026/10/16' AND timestamp < '2026/11/15'
    AND useridentity.type = 'IAMUser'
    AND useridentity.accesskeyid LIKE 'AKIA%'
),
today AS (
  SELECT
    useridentity.accesskeyid AS key_id,
    useridentity.arn AS who,
    sourceipaddress,
    split_part(sourceipaddress, '.', 1) || '.' || split_part(sourceipaddress, '.', 2) AS net,
    min(eventtime) AS first_call,
    count(*) AS calls
  FROM cloudtrail_org
  WHERE timestamp = '2026/11/15'
    AND useridentity.type = 'IAMUser'
    AND useridentity.accesskeyid LIKE 'AKIA%'
  GROUP BY 1, 2, 3, 4
)
SELECT t.*
FROM today t
LEFT JOIN baseline b ON t.key_id = b.key_id AND t.net = b.net
WHERE b.key_id IS NULL
ORDER BY first_call;
```

Only long-lived keys (`AKIA…`) are checked; role sessions (`ASIA…`) rotate constantly.

## Limits
- A key younger than 30 days looks new everywhere.
- Calls AWS makes on your behalf show a service name instead of an IP; filter them if they appear.
