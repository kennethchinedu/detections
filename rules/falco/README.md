# Falco rules

Falco reads system calls, not log files, so these rules are tested against a running cluster instead of
fixtures.

| Test | Command | Expected |
|---|---|---|
| positive | `kubectl -n pygoat exec deploy/pygoat -- sh -c id` | `Shell in PyGoat container … shell=sh` |
| negative | `kubectl -n default run tmp --rm -it --image=busybox -- sh -c id` | no alert |
