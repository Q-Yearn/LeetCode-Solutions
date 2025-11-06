class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == "]":
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False