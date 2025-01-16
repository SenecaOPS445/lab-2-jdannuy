#!/usr/bin/env python3
if True:
    print('This print is a part of the if statement')
if False:
    print('This first print statement will never run')
    print('This second print statement will also not run')
print('This print statement will run')
password = input('Please enter a secret password: ')
if password == 'P@ssw0rd':
    print('You have successfully used the right password')
import sys

print(len(sys.argv))

if len(sys.argv) != 10:
    print('You do not have 10 arguments')
    sys.exit()

