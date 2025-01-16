#!/usr/bin/env python3
# Author: [Jhanlyn Brita Dannuy]
# Author ID: [121247225]
# Date Created: [2025/01/15]

import sys

if len(sys.argv) < 2:
    print("Error: Please provide a starting value for the countdown.")
    sys.exit(1)

timer = int(sys.argv[1])
while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")
