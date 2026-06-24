class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charSet = set()
        n = len(s)

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            curLongest = (r - l) + 1
            longest = max(longest, curLongest)
            charSet.add(s[r])
        return longest