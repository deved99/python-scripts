#!/usr/bin/env python
from subprocess import run
suspend = ["systemctl", "suspend"]
lock = ["env", "XSECURELOCK_NO_COMPOSITE=1","xsecurelock"]
checklock = ["pidof", lock[0]]

check = run(checklock)
if check.returncode != 0:
    run(lock)
