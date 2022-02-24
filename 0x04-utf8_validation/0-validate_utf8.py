#!/usr/bin/python3
"""
Define validUTF8(data) function that validates whether a
string of ints represents a valid UTF-8 encoding.
"""
from itertools import takewhile


def int_to_bits(nums):
    """
    Helper function
    Convert ints to bits
    """
    for num in nums:
        bits = []
        mask = 1 << 8  # cause we have 8 bits per byte. adds up to (11111111)
        while mask:
            mask >>= 1
            bits.append(bool(num & mask))
        yield bits


def validUTF8(data):
    """
    Takes a list of ints and returns true if the list is
    a valid UTF-8 encoding, else returns false
    Args:
        data : List of ints representing possible UTF-8 encoding
    Return:
        bool : True or False
    """
    bits = int_to_bits(data)
    for byte in bits:
        # if single byte char, then valid. continue
        if byte[0] == 0:
            continue

        # if here, byte is multi-byte char
        ones = sum(takewhile(bool, byte))
        if ones <= 1:
            return False
        if ones >= 4:  # UTF-8 can be 1 to 4 bytes long
            return False

        for _ in range(ones - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
