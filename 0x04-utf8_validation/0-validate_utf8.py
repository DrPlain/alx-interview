#!/usr/bin/python3
"""
Determine if a given data set is a valid utf8 encoding
"""


def validUTF8(data):
    """ Check if data represents valid utf8 encoding """
    num_bytes_to_check = 0

    for byte in data:
        if num_bytes_to_check == 0:
            # With a right sift by 7 positions, all single byte
            # characters starts with a 0
            if (byte >> 7) == 0b0:
                continue
            # To examine if the first 3 bits starts with '110'
            elif (byte >> 5) == 0b110:
                num_bytes_to_check = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_to_check = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_to_check = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes_to_check -= 1

    return num_bytes_to_check == 0
