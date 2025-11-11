class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        number = []
        # 在for循环里手动修改a不会发生改变
        a = 0
        while a < len(s):
            if s[a].isdigit():
                numstr = s[a]
                a += 1
                while s[a].isdigit():
                    numstr += s[a]
                    a += 1
                number.append(int(numstr))
                a -= 1
            elif s[a] == '[' or ord('a') <= ord(s[a]) <= ord('z'):
                result.append(s[a])
            else:
                for i in range(len(result)-1, -1, -1):
                    if result[i] == '[':
                        mul = number.pop()
                        result = result[:i] + result[i+1:] * mul
                        break
            a += 1
        return ''.join(result)

            