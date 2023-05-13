#!/usr/bin/python3
"""
Log Parser
Reads from stdin line by line and computes metrics
"""
from sys import stdin

count = 0
file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0
                }


def print_output():
    """
    Helper function to print computed statistics
    """
    print("File size: {}".format(file_size))
    for k, v in status_codes.items():
        if v != 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    try:
        for line in stdin:
            line = line.rstrip('\n')
            try:
                status_code = line.split()[-2]
                size = int(line.split()[-1])
            except Exception:
                pass
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
            file_size += size
            count = count + 1
            if count % 10 == 0:
                print_output()
    except KeyboardInterrupt:
        print_output()
        raise
    print_output()
