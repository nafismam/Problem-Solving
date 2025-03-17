from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSub to the first element of the array
        # This stores the maximum sum of any subarray found so far
        maxSub = nums[0]

        # Current sum of the subarray (will be reset if it becomes negative)
        curSum = 0

        # Iterate through each number in the array
        for n in nums:
            # If curSum becomes negative, reset it to 0 to start a new subarray
            if curSum < 0:
                curSum = 0

            # Add the current number `n` to curSum
            curSum += n

            # Update maxSub to the maximum of itself and the current sum
            maxSub = max(maxSub, curSum)

        # Return the maximum subarray sum found
        return maxSub


# Driver code with prewritten input
if __name__ == "__main__":
    # Prewritten input array
    nums = [2, -3, 4, -2, 2, 1, -1, 4]
    print(f"Input array: {nums}")

    # Create an instance of the Solution class
    solution = Solution()

    # Call the maxSubArray function and store the result
    max_sum = solution.maxSubArray(nums)

    # Print the result
    print(f"Maximum Subarray Sum: {max_sum}")
