# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

#     The minimum value in the subarray is equal to minK.
#     The maximum value in the subarray is equal to maxK.

# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        prevMinInd = prevMaxInd = cur_ind = -1

        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                cur_ind = i
            if n == minK:
                prevMinInd = i
            if n == maxK:
                prevMaxInd = i
            
            start_ind = min(prevMaxInd, prevMinInd)

            if start_ind > cur_ind:
                result += (start_ind - cur_ind)

        return result