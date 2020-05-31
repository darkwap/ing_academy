# Card number validity can be checked using Luhn algorithm.
# https://en.wikipedia.org/wiki/Luhn_algorithm
#
# Your task is to implement this algorithm.
#
# Write function to validate credit card numbers:
#   def solution(card_number):
#
# Variable card_number will be provided as string (no spaces inside).
# Function should return True for valid card number, and False for invalid.
#
# Sample data:
# Valid card numbers
# 4111111111111111
# 5500000000000004
#
# Invalid card numbers
# 4198786787558765
# 9875787643456354
import numpy as np

def solution(card_number):
    card_num_array = np.frombuffer(str.encode(card_number), dtype=np.uint8)
    card_num_array = card_num_array - 48
    output_array = []
    length = card_num_array.shape[0]
    for i in range(1, length + 1):
        if i % 2 == 0:
            output_array.append(1)
        else:
            output_array.append(2)
    mult_array = card_num_array * output_array
    mult_array = np.where(mult_array > 9, mult_array - 9, mult_array)
    if mult_array.sum() % 10 != 0:  # append control number
        card_num_array = np.append(card_num_array, 10 - mult_array.sum() % 10, axis=None)
        output_array = []
        length = card_num_array.shape[0]
        for i in range(1, length + 1):
            if i % 2 == 0:
                output_array.append(2)
            else:
                output_array.append(1)
        mult_array = card_num_array * output_array
        mult_array = np.where(mult_array > 9, mult_array - 9, mult_array)
        if mult_array.sum() % 10 == 0:
            return True
        else:
            return False
    return True
