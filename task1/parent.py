#!/usr/bin/python3

import os
import sys
import random

argvs = int(sys.argv[1])

for i in range(0, argvs):
    child = os.fork()
    if child == 0:
        os.execl("./child.py", "child.py", str(random.randint(5, 10)))
    print(f"Parent [{os.getpid()}]: I ran children process with PID {child}")

while argvs > 0:
    child_pid, status = os.wait()
    status = status // 256
    print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.")
    if status > 0:
        child = os.fork()
    else:
        argvs = argvs - 1
    if child == 0:
        os.execl("./child.py", "child.py", str(random.randint(5, 10)))
    print(f"Parent [{os.getpid()}]: I ran children process with PID {child}")
