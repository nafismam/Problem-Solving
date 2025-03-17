from typing import List  # Import List for type hinting

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]  # Initialize global max and min with the first element
        curMax, curMin = 0, 0  # Initialize current max and min subarray sums as 0
        total = 0  # Variable to store the total sum of the array

        for n in nums:  # Iterate through each number in the array
            curMax = max(curMax + n, n)  # Update current max subarray sum
            curMin = min(curMin + n, n)  # Update current min subarray sum
            total += n  # Add the current number to the total sum
            globMax = max(globMax, curMax)  # Update global max subarray sum
            globMin = min(globMin, curMin)  # Update global min subarray sum

        # If the global max is positive, consider the circular case
        if globMax > 0:
            return max(globMax, total - globMin)  # Return the maximum of the global max and circular max sum
        else:
            return globMax  # If all elements are negative, return the global max (largest single element)

# Example usage
nums = [5, -3, 5]  # Premade input array
solution = Solution()  # Create an instance of the Solution class
result = solution.maxSubarraySumCircular(nums)  # Call the method with the input array
print("Maximum circular subarray sum:", result)  # Output the result
