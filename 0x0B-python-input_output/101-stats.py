#!/usr/bin/python3
""" Python script that reads stdin line by line and computes metrics. """

import sys
import signal

def signal_handeler(signum, frame):
    """Prints the stats when receiving a SIGINT signal."""
    print_stats(total, status_codes)
    sys.exit(0)

def print_stats(total, status_codes):
    print("File size: {}".format(total))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handeler)
    total = 0
    count = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        for line in sys.stdin:
            try:
                line = line.split()
                count += 1
                total += int(line[-1])
                status_code = int(line[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                if count % 10 == 0:
                    print_stats(total, status_codes)                 
            except:
                pass
    except KeyboardInterrupt:
        print_stats(total, status_codes)