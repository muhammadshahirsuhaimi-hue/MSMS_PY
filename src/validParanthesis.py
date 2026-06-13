class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #early return
        if len(s) % 2 != 0:
            return False

        stack = []
        prevChar = ''
        for char in s:
            if char == '(' or char == '[' or char == "{":
                stack.append(char)
                prevChar = char
            else:
                if char == ')' and prevChar == '(':
                    stack.pop()
                elif char == ']' and prevChar == '[':
                    stack.pop()
                elif char == '}' and prevChar == '{':
                    stack.pop()
                else:
                    return False
                
                if len(stack) == 0:
                    prevChar = ''
                else:
                    prevChar = stack[-1]
                

        return len(stack) == 0
            