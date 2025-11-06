class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        stack = []
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack