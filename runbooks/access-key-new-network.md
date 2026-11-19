# Access key used from a new network

**Hunt:** [aws_access_key_new_source](../hunts/aws_access_key_new_source.md) · **Severity:** medium · **ATT&CK:** T1078.004

## What it means
A long-lived access key was used from a network it hasn't used in the last 30 days. Leaked keys usually show
up here first.

## Triage
1. Whose key is it, and what can it do? Check the user's attached and inline policies.
2. What network is the new IP? A VPS or Tor exit is far worse than a new mobile network.
3. What calls came from the new IP? Look for `GetSessionToken`, `ListBuckets` and `GetCallerIdentity`.
4. Is the key in a public repo? Search GitHub for the key ID.

## Benign if
The owner confirms a new location or server, and the calls match their normal work.

## Escalate if
The owner doesn't recognise it, the IP is a hosting provider or Tor, or the key created temporary credentials.

## Contain
1. Deactivate the key.
2. Attach a deny-all policy to the user. This also blocks temporary credentials the key already created.
3. Check for persistence: new users, keys, roles or bucket policies.
