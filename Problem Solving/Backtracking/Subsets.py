from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Helper function to perform backtracking
        def backtrack(index, current):
            # Add the current subset to the result
            result.append(current[:])  # Make a copy to avoid changes during recursion
            
            # Loop through the available choices starting from the current index
            for i in range(index, len(nums)):
                # Include nums[i] in the current subset
                current.append(nums[i])
                
                # Recursively explore further subsets starting with the current element included
                backtrack(i + 1, current)
                
                # Backtrack: remove the last added element to explore other combinations
                current.pop()

        # Initialize the result list to store all subsets
        result = []
        
        # Start the backtracking process with an empty subset
        backtrack(0, [])
        
        # Return the list of all generated subsets
        return result


# Test the Solution with Example Inputs
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(f"Subsets of {nums1}: {Solution().subsets(nums1)}")
    
    # Test Case 2
    nums2 = [7]
    print(f"Subsets of {nums2}: {Solution().subsets(nums2)}")
    
    # Test Case 3
    nums3 = [4, 5]
    print(f"Subsets of {nums3}: {Solution().subsets(nums3)}")
