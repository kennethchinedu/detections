# Shell in application container

**Rule:** [pygoat_shell_in_container](../rules/falco/pygoat_shell_in_container.yaml) · **Severity:** warning · **ATT&CK:** T1059

## What it means
A shell started inside the app container. The app never runs a shell, so someone is running commands there:
`kubectl exec` or an exploited command injection.

## Triage
1. Read the parent process in the alert. `python` or `gunicorn` as parent means the app spawned it: likely RCE.
2. Read the command line. `id`, `whoami`, `curl` and `wget` are typical first steps.
3. Was anyone doing a `kubectl exec`? Check the Kubernetes audit log for the user.
4. Did the pod make network connections it shouldn't? Check NetworkPolicy deny logs.

## Benign if
An engineer ran `kubectl exec` during approved debugging, and the audit log shows them.

## Escalate if
The parent is the app process, nobody ran `kubectl exec`, or the commands reach out to the network.

## Contain
1. Isolate the pod with a deny-all NetworkPolicy. Don't delete it yet: you lose the evidence.
2. Check the service account token and rotate any secrets mounted in the pod.
3. Scale up a clean replica, then capture and delete the compromised pod.
