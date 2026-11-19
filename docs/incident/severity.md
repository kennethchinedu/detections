# Severity

Decide severity from the facts, not from how worried you feel. When unsure, pick the higher level: lowering a
SEV1 takes minutes, a breach handled as a SEV3 loses hours.

## How to decide

1. Is someone doing harm, or did they? **No:** it's a finding, not an incident. SEV4, backlog.
2. Is customer data or money affected, or is a legal clock running? **Yes:** SEV1.
3. Is the compromise confirmed? **Yes:** SEV2. **No, only suspicious:** SEV3.

Stolen credentials used by someone else are always confirmed, even if they've only looked around.

## Levels

| Level | Means | Example | Response |
|---|---|---|---|
| SEV1 | Active attack, customer data stolen or lost, or a regulator clock running | Bucket of customer receipts deleted with a ransom note | Page IC now. Updates every 30 min. Leadership and legal within 1 h. |
| SEV2 | Confirmed compromise, contained or not yet touching customers | Role credentials used from a Tor exit, only `ListBuckets` so far | Page on-call. Updates every 2 h. Security lead told. |
| SEV3 | Suspicious, not confirmed | Console login without MFA from a known IP | Ticket. Investigate in working hours. |
| SEV4 | Weakness with no attacker | Sandbox buckets without default encryption | Backlog with an owner and a due date. |

Severity can change during an incident. Say so in the next update, with the reason.
