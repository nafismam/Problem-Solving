class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: `l` at the start (smallest element) and `r` at the end (largest element)
        l, r = 0, len(numbers)-1
        
        # Loop until the two pointers meet
        while l < r:
            # Compute the sum of the current left and right elements
            sum2 = numbers[l] + numbers[r]
            
            # If the sum is greater than the target, move the right pointer left (to reduce the sum)
            if sum2 > target:
                r = r - 1
            
            # If the sum is less than the target, move the left pointer right (to increase the sum)
            elif sum2 < target:
                l = l + 1
            
            # If the sum equals the target, return the indices (+1 since the problem expects 1-based indexing)
            else:
                return [l+1, r+1]
        
        # If no solution is found (though the problem guarantees one), return an empty list
        return []