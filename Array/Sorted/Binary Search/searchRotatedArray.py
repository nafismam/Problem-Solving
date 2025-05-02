# Define a class named Solution
class Solution:
    # Define a method 'search' that takes a list of integers 'nums' and an integer 'target'
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers: 'l' at the start, and 'r' at the end of the array
        l, r = 0, len(nums) - 1

        # Loop until the pointers meet or cross
        while l <= r:
            # Find the middle index
            m = (l + r) // 2

            # If the target is found at the middle, return the index
            if target == nums[m]:
                return m

            # Check if the left portion from 'l' to 'm' is sorted
            if nums[l] <= nums[m]:
                # If target is outside the range of the left portion, search in the right half
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                # Else, narrow the search to the left portion
                else:
                    r = m - 1

            # Else, the right portion from 'm' to 'r' must be sorted
            else:
                # If target is outside the range of the right portion, search in the left half
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                # Else, narrow the search to the right portion
                else:
                    l = m + 1

        # If the target was not found, return -1
        return -1
