class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # `l` points to the position where the next unique element should be placed.
        # Start at `1` because the first element is always unique.
        l = 1

        # `r` scans the array starting from the second element.
        for r in range(1, len(nums)):
            # If the current element (`nums[r]`) is different from the previous (`nums[r-1]`),
            # it means we've found a new unique element.
            if nums[r] != nums[r - 1]:
                # Place this unique element at position `l`.
                nums[l] = nums[r]
                # Move `l` forward to the next position for future unique elements.
                l += 1

        # `l` now represents the number of unique elements.
        return l