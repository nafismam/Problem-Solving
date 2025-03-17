class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers
        l = 0  # Pointer starting at the beginning of the string
        r = len(s) - 1  # Pointer starting at the end of the string

        # Process the string until the two pointers meet
        while l < r:
            # Move the left pointer forward if the current character is not alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # Move the right pointer backward if the current character is not alphanumeric
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            # Compare the characters at the left and right pointers (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False  # If the characters don't match, it's not a palindrome

            # Move both pointers closer to the center
            l, r = l + 1, r - 1

        return True  # If the loop completes, the string is a palindrome

    def alphaNum(self, c):
        # Check if the character is alphanumeric (A-Z, a-z, or 0-9)
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
