class NumArray:
    
    # Constructor method to initialize the object with the input list 'nums'
    def __init__(self, nums: List[int]):
        self.prefix = []          # This list will store the prefix sums
        total = 0                 # 'total' keeps track of the running sum
        for n in nums:           # Loop through each number in the input list
            total = total + n    # Add the current number to the total
            self.prefix.append(total)  # Store the running total in the prefix list

    # Method to return the sum of elements from index 'left' to 'right' (inclusive)
    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]         # Sum of all elements up to 'right'
        if left > 0:
            preLeft = self.prefix[left - 1]   # Sum of elements before 'left'
        else:
            preLeft = 0                       # If 'left' is 0, there's nothing before it
        return (preRight - preLeft)           # Subtract to get the sum from left to right


# Example usage:
# obj = NumArray(nums)         # Create an object by passing the input list
# param_1 = obj.sumRange(left, right)  # Get the sum between 'left' and 'right' indices
