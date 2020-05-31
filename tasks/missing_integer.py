# Write a function:
#
#     def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].
#
import numpy as np


def missing_val(A, low_idx, high_idx):
    if high_idx < low_idx:
        return low_idx + 1

    idx = int(np.floor((high_idx + low_idx) / 2))
    '''print('array index '+str(idx))
    print(A[low_idx:high_idx])
    print('low_idx '+str(low_idx))
    print('high_idx '+str(high_idx))'''

    if A[idx] == idx + 1:
        # print('we took higher part ')
        return missing_val(A, idx + 1, high_idx)
    else:
        # print('we took lower part')
        return missing_val(A, low_idx, idx - 1)


def solution(A):
    #sorted and unique
    A = sorted(set(A))
    A = np.array(A)
    #grater than zero
    A = A[A > 0]
    return missing_val(A, 0, len(A)-1)
