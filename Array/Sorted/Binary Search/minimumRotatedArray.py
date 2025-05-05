class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize left and right pointers to start and end of array
        l, r = 0, len(nums)-1
        
        # Binary search loop (while left pointer hasn't met right pointer)
        while l < r:
            # Calculate middle index
            m = (l + r) // 2
            
            # If middle element is less than right element, 
            # the minimum is in the left half (including middle)
            if nums[m] < nums[r]:
                r = m
            # Else, the minimum is in the right half (excluding middle)
            else:
                l = m + 1
                
        # When loop ends, left pointer points to the minimum element
        return nums[l]