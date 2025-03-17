class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in the current substring
        charSet = set()
        # Left pointer of the sliding window
        left = 0
        # Variable to store the result (maximum length)
        result = 0

        # Iterate over the string using the right pointer
        for right in range(len(s)):
            # If the character at `right` already exists in the set (duplicate):
            while s[right] in charSet:
                # Remove the character at `left` pointer from the set
                charSet.remove(s[left])
                # Move the left pointer to shrink the window
                left += 1
            # Add the current character `s[right]` to the set
            charSet.add(s[right])
            # Update the result with the length of the current window
            result = max(result, right - left + 1)

        # Return the length of the longest substring without repeating characters
        return result


# Function to take input and print the output
if __name__ == "__main__":
    s = input("Enter the string: ")
    solution = Solution()
    length = solution.lengthOfLongestSubstring(s)
    print(f"Length of the longest substring without repeating characters: {length}")
