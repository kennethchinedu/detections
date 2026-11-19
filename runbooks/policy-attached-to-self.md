# IAM policy attached to self

**Rule:** [aws_iam_policy_attached_to_self](../rules/aws/aws_iam_policy_attached_to_self.yml) · **Severity:** high · **ATT&CK:** T1098

## What it means
An identity gave a policy to itself. Permissions should come from an admin or a pipeline, never from the
identity itself. This is a common privilege escalation path.

## Triage
1. What policy was attached? `AdministratorAccess` or anything with `"*"` is the worst case.
2. Is the caller a pipeline role managing itself by design? If so, that design is its own risk.
3. Where did the call come from: a known build runner or laptop, or a new IP?
4. What did the identity do after the change?

## Benign if
A known pipeline role, applying a reviewed Terraform change, from the CI runner.

## Escalate if
A human user or unknown source, no matching change, or high-privilege actions right after.

## Contain
1. Detach the policy: `aws iam detach-user-policy` or `detach-role-policy`.
2. Deactivate the identity's keys and attach a deny-all policy.
3. Revoke active sessions if it's a role.
