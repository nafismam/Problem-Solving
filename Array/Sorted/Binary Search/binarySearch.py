#neetcode binary search

# Define a class named Solution
class Solution:
    # Define a method 'search' that takes a list of integers 'nums' and an integer 'target'
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers, L (left) at 0 and R (right) at the length of nums
        L, R = 0, len(nums) - 1  # ← corrected from 'len(nums)' to 'len(nums) - 1' to prevent index error

        # Continue the loop as long as the left pointer is less than or equal to the right pointer
        while L <= R:
            # Calculate the middle index between L and R
            m = (L + R) // 2

            # If the target is greater than the middle element, discard the left half
            if target > nums[m]:
                L = m + 1

            # If the target is less than the middle element, discard the right half
            elif target < nums[m]:
                R = m - 1

            # If the middle element is the target, return its index
            else:
                return m

        # If the loop ends without finding the target, return -1
        return -1
