class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Loop through, keep only letters/numbers, and lowercase them
        finalString = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(finalString) - 1
        while left < right:
            if finalString[left] != finalString[right]:
                return False
            left += 1
            right -= 1

        return True