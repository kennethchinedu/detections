# Escalation and handover

## Escalation

Decided now so nobody has to think about it at 03:00.

| Trigger | Pull in |
|---|---|
| Alert not acknowledged in 15 min | Secondary on-call |
| SEV1 or SEV2 declared | IC, then security lead, then CTO |
| Personal data may be involved | DPO and legal, immediately. The GDPR 72 h clock starts at awareness |
| Extortion or ransom demand | Legal, exec, police. No contact with the attacker without legal |
| Compromised AWS account or abuse | AWS Support, security case |
| Fix needs a team you don't own | That team's on-call |

DPO: Data Protection Officer. Owns GDPR compliance, decides if a breach is reportable, writes the regulator
notice, and is the regulator's contact.

## Handover

When the IC changes (shift end, fatigue, long incident). The new IC should not need to ask anything.

```
Severity / state: <SEV#, contained or not>
Done:             <actions with times>
In progress:      <what, who>
Open decisions:   <what's waiting, deadlines: GDPR clock, next update>
Risks:            <what could go wrong next>
```

Close it in the channel: **"<name> is IC as of <HH:MM>."**

The outgoing IC stays reachable for 30 minutes.
