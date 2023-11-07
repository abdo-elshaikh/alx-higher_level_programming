#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

import sys


if __name__ == "__main__":
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    file_size = 0
    number_of_lines = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        tokens = line.split()
        status_codes[int(tokens[-2])] += 1
        file_size += int(tokens[-1])
        number_of_lines += 1
        if number_of_lines == 10:
            print("File size: {}".format(file_size))
            for status_code, count in status_codes.items():
                print("{}: {}".format(status_code, count))
            number_of_lines = 0
