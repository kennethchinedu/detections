# Roles

Every incident has one person in each role. On a small team one person can hold two, but the incident
commander never does hands-on work. If the IC needs to debug, they hand over command first, out loud.

| Role | Job | Not their job |
|---|---|---|
| Incident commander (IC) | Sets severity and priorities, assigns work, decides when to escalate and close | Running commands |
| Ops lead | Investigates and contains, reports findings to the IC | Talking to customers |
| Comms lead | Writes every update on the IC's schedule | Deciding what's true |
| Scribe | Keeps the timeline: every decision and action with its time | Anything else |

Allowed pairs on a small team: comms + scribe, ops + scribe. Never IC + ops.

## IC checklist

**First 15 minutes**
- [ ] Open the incident channel and say "I'm IC"
- [ ] Set severity from [severity.md](severity.md)
- [ ] Name the ops lead, comms lead and scribe
- [ ] Agree the first containment step and who does it
- [ ] Set the next update time

**Every update cycle**
- [ ] What do we know now?
- [ ] What are we doing, and who's on it?
- [ ] Has severity changed?
- [ ] Verify anything reported as done before it goes in an update

**Closing**
- [ ] Attacker access removed and confirmed
- [ ] Systems restored and watched for at least one update cycle
- [ ] Final update sent
- [ ] Post-mortem owner and date set (within 24 h for SEV1 and SEV2)
