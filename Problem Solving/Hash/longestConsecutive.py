from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list `nums` into a set for O(1) lookups
        numSet = set(nums)  # This allows quick checks for the presence of a number
        longest = 0  # Variable to store the length of the longest consecutive sequence

        # Iterate over each number `n` in the original list `nums`
        for n in nums:
            # Check if `n` is the start of a sequence (i.e., no number `n - 1` exists)
            if (n - 1) not in numSet:
                # `n` is the start of a new consecutive sequence
                length = 0  # Length of the current sequence

                # Count the length of the sequence starting at `n`
                while (n + length) in numSet:
                    length += 1  # Increment the sequence length

                # Update `longest` if the current sequence is longer than the previous longest
                longest = max(length, longest)

        # Return the length of the longest consecutive sequence found
        return longest
