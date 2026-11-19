# What done means

## An alert is done when
1. It has a verdict: true positive, false positive, or benign true positive (real, but allowed).
2. The reason is written down, with the evidence.
3. True positive: an incident is opened or it's escalated.
4. False positive: a tuning ticket is opened against the rule.

## An incident is done when
1. Contained and verified (e.g. `AccessDenied` seen in the logs, not "should be blocked").
2. Recovered: service and data back, or the loss recorded.
3. Notifications sent: regulator, customers, controller, as required.
4. Post-mortem written within 24 h.
5. Every action has a named owner and a date.

Data that was copied out can't be recovered. Record it, and add an action to monitor for it (leak sites,
paste sites) with an owner and an end date.

Closing the incident doesn't close the actions. They're tracked until shipped.
