#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys
from collections import defaultdict

if __name__ == "__main__":
    status_counts = defaultdict(int)
    total_file_size = 0
    total_lines_read = 0
    output_buffer = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        tokens = line.split()
        status_code = int(tokens[-2])
        file_size = int(tokens[-1])

        status_counts[status_code] += 1
        total_file_size += file_size
        total_lines_read += 1

        if total_lines_read % 10 == 0:
            output_buffer.append("File size: {}".format(total_file_size))
            for status_code, count in sorted(status_counts.items()):
                if count == 0:
                    continue
                output_buffer.append("{}: {}".format(status_code, count))

            print("\n".join(output_buffer))
            output_buffer = []

    if output_buffer:
        print("\n".join(output_buffer))
