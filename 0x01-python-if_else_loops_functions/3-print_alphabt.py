#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char != 'q' or char != 'e':
        print('{:c}'.format(char), end='')