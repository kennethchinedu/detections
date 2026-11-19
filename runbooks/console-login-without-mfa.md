# Console login without MFA

**Rule:** [aws_console_login_without_mfa](../rules/aws/aws_console_login_without_mfa.yml) · **Severity:** medium · **ATT&CK:** T1078.004

## What it means
An IAM user or root signed in to the console with only a password. A stolen password is enough to get in.

## Triage
1. Which identity? Root is always serious; an IAM user means MFA isn't enforced for them.
2. Is the IP and location normal for this person? Compare with their last 30 days.
3. Ask the user directly, on a channel other than email: was this you?
4. What did they do after logging in? Look for IAM, CloudTrail or S3 policy changes.

## Benign if
The user confirms, from a known IP, and did normal work. Still fix it: enforce MFA on the user.

## Escalate if
The user didn't log in, the IP is new, or they changed IAM or logging after signing in.

## Contain
1. Reset the password and remove console access: `aws iam delete-login-profile --user-name <user>`
2. Attach a deny-all policy to the user until reviewed.
3. For root: change the password, set up MFA, and check for root access keys.

## Known false positive
SSO users always show `MFAUsed: No`, because MFA happens at the identity provider. The rule filters them out.
