#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """
    prints all the names defined by the compiled arguments.
    """
    args = sys.argv[1:]
    sum = 0
    for i in range(len(args)):
        sum += int(args[i])
    print(sum)
