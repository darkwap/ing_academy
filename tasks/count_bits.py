# Write a function:
#
#     def solution(A, B)
#
# that, given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation
# of the number A * B.
#
# For example, given A = 3 and B = 7 the function should return 3, because the binary representation of
# A * B = 3 * 7 = 21 is 10101 and it contains three bits set to 1.
#
# Assume that:
# A and B are integers within the range [0..100,000,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
import numpy as np

def solution(A, B):
    bin_array = np.frombuffer(str.encode(np.binary_repr(A * B)), dtype=np.uint8)
    bin_array = bin_array - 48
    return (bin_array == 1).sum()

    ''' more low level version
    result = a*b
       mask = 1
       count_ones = 0
       for i in range(len(np.binary_repr(result))):
           if np.bitwise_and(result,mask) == 1:
               count_ones = count_ones + 1
           result = np.right_shift(result,1)
       return count_ones'''

