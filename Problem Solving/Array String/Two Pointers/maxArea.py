from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1  # Initialize right pointer to the last index

        while left < right:
            # Calculate the area between the two pointers
            area = (right - left) * min(heights[left], heights[right])
            result = max(result, area)  # Update the maximum area

            # Move the pointer pointing to the shorter height
            if heights[left] <= heights[right]:
                left += 1  # Move `left` to the right
            else:
                right -= 1  # Move `right` to the left

        return result
