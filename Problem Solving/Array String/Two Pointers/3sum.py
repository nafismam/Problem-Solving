from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # List to store the unique triplets
        result = []
        # Sort the array to use the two-pointer technique
        nums.sort()  # Sorting helps us efficiently find triplets

        # Iterate through the array to pick the first element of the triplet
        for i in range(len(nums) - 2):
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip if the current element is the same as the previous

            # Two-pointer approach for the remaining two elements
            left = i + 1  # Next element after `i`
            right = len(nums) - 1  # Last element in the array

            # Check pairs with the current `nums[i]`
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # If the sum is less than 0, move the `left` pointer to increase the sum
                    left += 1
                elif total > 0:
                    # If the sum is greater than 0, move the `right` pointer to decrease the sum
                    right -= 1
                else:
                    # Found a triplet that sums to 0
                    result.append([nums[i], nums[left], nums[right]])
                    # Move both pointers after storing the triplet
                    left += 1
                    right -= 1

                    # Skip duplicates for the `left` pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the `right` pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

# Driver code with prewritten input
if __name__ == "__main__":
    # Prewritten input array
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"Input array: {nums}")

    # Create an instance of the Solution class
    solution = Solution()

    # Call the threeSum function and store the result
    output = solution.threeSum(nums)

    # Print the result
    print(f"Triplets that sum to 0: {output}")
