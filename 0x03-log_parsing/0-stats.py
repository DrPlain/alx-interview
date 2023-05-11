#!/usr/bin/python3
""" Log Parser
Reads from stdin line by line and computes metrics
"""
from sys import stdin
import datetime
import re

count = 0
parameters = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
    'size': 0
}


def check_format(line):
    """Parses line from stdin and checks if its required format
    Returns:
        List of [ip-address, date, status_code, file_size]
        as strings
    """

    line = line.rstrip('\n')
    const_string = '"GET /projects/260 HTTP/1.1"'
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    if const_string in line:
        try:
            line = line.replace(const_string, '')
            tokens = line.split(' - ')
            ip_address = tokens[0]
            tokens = tokens[1].split(' ')
            date = tokens[0].lstrip('[') + " " + tokens[1].rstrip(']')
            code = tokens[3]
            size = tokens[4]
        except Exception as err:
            return False
        else:

            ip_match = re.match(ip_pattern, ip_address)
            if ip_match is None:
                return False
            try:
                parsed_date = datetime.datetime.strptime(
                    date, "%Y-%m-%d %H:%M:%S.%f")
            except ValueError as err:
                return False
            if code.isdigit():
                if int(code) not in status_codes:
                    return False
            else:
                return False

            if size.isdigit():
                pass
            else:
                return False
            return [ip_address, date, code, size]
    else:
        return False


def print_output():
    """ Helper function to print computed statistics"""
    print(f"File size: {parameters['size']}")
    for k, v in parameters.items():
        if k != 'size' and v != 0:
            print(f"{k}: {v}")


try:
    for line in stdin:
        tokens = check_format(line)
        if tokens:
            if tokens[2] == '200':
                parameters['200'] += 1
            elif tokens[2] == '301':
                parameters['301'] += 1
            elif tokens[2] == '400':
                parameters['400'] += 1
            elif tokens[2] == '401':
                parameters['401'] += 1
            elif tokens[2] == '403':
                parameters['403'] += 1
            elif tokens[2] == '404':
                parameters['404'] += 1
            elif tokens[2] == '405':
                parameters['405'] += 1
            elif tokens[2] == '500':
                parameters['500'] += 1

            parameters['size'] += int(tokens[3])
            count = count + 1
            if count % 3 == 0:
                print_output()
        else:
            continue
except KeyboardInterrupt:
    print_output()
