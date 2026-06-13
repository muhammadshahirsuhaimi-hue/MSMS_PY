from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
    
    #manual way of creating dict
class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str

        :type t: str

        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            count[sChar] = count.get(sChar, 0) + 1
            count[tChar] = count.get(tChar, 0) - 1

        # If it's a true anagram, every single count must be exactly 0
        for val in count.values():
            if val != 0:
                return False
        return True