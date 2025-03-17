# LEETCODE 53 Maximum Subarray

from typing import List  # Import List type hint for defining function input type

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]  # Initialize maxSum with the first element of the list (to handle edge cases where all elements are negative)
        current = 0  # Variable to keep track of the current subarray sum

        for n in nums:  # Iterate through each number in the list
            current = max(current, 0)  # Reset current to 0 if it becomes negative (start a new subarray)
            current += n  # Add the current number to the current subarray sum
            maxSum = max(maxSum, current)  # Update maxSum if the current subarray sum is greater
        return maxSum  # Return the maximum subarray sum
# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Premade input array
solution = Solution()  # Create an instance of the Solution class
result = solution.maxSubArray(nums)  # Call the maxSubArray method
print("Maximum subarray sum:", result)  # Output the result
