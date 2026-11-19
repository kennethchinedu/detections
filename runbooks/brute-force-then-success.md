# Brute force then successful login

**Rule:** [aws_console_brute_force_then_success](../rules/aws/aws_console_brute_force_then_success.yml) · **Severity:** high · **ATT&CK:** T1110

## What it means
Five or more failed console logins from one IP, then a successful one from the same IP within 30 minutes.
Someone may have guessed the password.

## Triage
1. Which account succeeded? Is it the same account the failures targeted?
2. Is the IP known? A shared office IP can mix one person's typos with another person's normal login.
3. Was there a password reset between the failures and the success?
4. What happened after the login?

## Benign if
The same user, from a known IP, who forgot their password and reset it.

## Escalate if
Unknown IP, no reset, or several accounts targeted from the same IP (password spraying).

## Contain
1. Remove the account's console access and force a password reset.
2. Attach a deny-all policy until the user confirms.
3. Block the IP in WAF or the network edge if it's still active.
