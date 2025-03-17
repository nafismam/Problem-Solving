from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HashMap (dictionary) to store the index of each number as we traverse
        hashMap = {}

        # Iterate over the list with both index `i` and element `n`
        for i, n in enumerate(nums):
            # Calculate the difference `d` needed to reach the target
            d = target - n  # d = target - current number

            # Check if the difference `d` exists in the hashMap
            if d in hashMap:
                # If it exists, return the indices of `d` and `n`
                return [hashMap[d], i]

            # Otherwise, store the index of the current number `n` in hashMap
            hashMap[n] = i  # Store `n` as the key and its index `i` as the value

        # Return nothing if no valid pair is found (though not expected for valid inputs)
        return
