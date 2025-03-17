from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1  # Initialize pointers

        while left < right:
            curSum = numbers[left] + numbers[right]  # Calculate the sum of the two pointers

            if curSum > target:
                right -= 1  # Move the right pointer left to reduce the sum
            elif curSum < target:
                left += 1  # Move the left pointer right to increase the sum
            else:
                return [left + 1, right + 1]  # Return 1-based indices

        # There is always a solution, so no need for a default return statement
