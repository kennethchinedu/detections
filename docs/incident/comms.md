# Comms

One incident, three audiences. Same facts, different detail.

Rules for every update:
- Only say what's true now. "Disabled", not "rotated", until it's rotated.
- Cause stays "under investigation" until it's confirmed.
- No names attached to mistakes.
- Always end with the next update time.

## Internal (incident channel)

Every 30 min on SEV1, every hour on SEV2.

```
[SEV#] <incident name>  <HH:MM>
Now:   <what we know: what, how many, since when>
Done:  <actions taken, with times>
Doing: <what's in progress, who>
Next update: <HH:MM>
```

Example:
```
[SEV1] receipts bucket deletion  07:40
Now:   48 DeleteObjects batches on hexpay-receipts from 45.137.x.x using backup-sync. ~48,000 objects.
Done:  07:09 deny-all on backup-sync, 07:10 AccessDenied confirmed. Logs exported.
Doing: list-object-versions to size recovery (Dami). GetObject hunt from the IP (Alex).
Next update: 08:10
```

## Customer

Only once facts are confirmed. Legal reviews before it goes out.

```
Subject: Important information about your <data>

On <date> we found that an unauthorised party accessed <what data> belonging to some of our customers,
including yours.

What happened: <one or two sentences, no technical detail>
What we've done: <stopped the access, restoring, working with authorities>
What you should do: <concrete steps, or "nothing at this time">
Questions: <contact>

We'll update you by <date>.
```

## Exec

Three lines. Impact first.

```
Impact:    <customers / records / money / legal exposure>
Status:    <contained or not, since when; next update time>
Decisions: <what you need from them, with deadlines>
```

Example:
```
Impact:    48,000 customer receipts copied and deleted; 41,000 being restored, 7,000 lost. Attacker
           threatens to publish unless paid 2 BTC.
Status:    Access cut off 07:09, confirmed, no activity since. Entry point under investigation.
           Next update 12:00.
Decisions: (1) Approve regulator notice by Sat 21 Nov 07:00 and customer notice.
           (2) Recommend no payment and no contact; legal and police engaged.
```

## Regulator (GDPR Art. 33)

Controller notifies within 72 h of becoming aware. If not everything is known, notify in phases.

- Nature of the breach, categories and rough number of people and records
- Contact point (DPO)
- Likely consequences
- Measures taken or proposed
