#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """
    prints all the names defined by the compiled arguments."""
    args = sys.argv[1:]
    if len(args) == 0:
        print(f'0 arguments.')
    else:
        if len(args) == 1:
            print(f'1 argument:')
        else:
            print(f'{len(args)} arguments.')
        for i in range(len(args)):
            print(f'{i + 1}: {args[i]}')
