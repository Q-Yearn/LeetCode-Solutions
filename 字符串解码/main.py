# 递归
class Solution(object):
    def __init__(self):
        self.src = ""
        self.ptr = 0

    def getDigits(self):
        """解析连续数字"""
        ret = 0
        while self.ptr < len(self.src) and self.src[self.ptr].isdigit():
            ret = ret * 10 + int(self.src[self.ptr])
            self.ptr += 1
        return ret

    def getString(self):
        """递归解析子串"""
        if self.ptr == len(self.src) or self.src[self.ptr] == ']':
            # String -> ε
            return ""

        cur = self.src[self.ptr]
        repTime = 1
        ret = ""

        if cur.isdigit():
            # String -> Digits [ String ] String
            repTime = self.getDigits()
            self.ptr += 1  # 跳过 '['
            str_ = self.getString()
            self.ptr += 1  # 跳过 ']'
            ret += str_ * repTime
        elif cur.isalpha():
            # String -> Char String
            ret = self.src[self.ptr]
            self.ptr += 1

        # 拼接后续字符串
        return ret + self.getString()

    def decodeString(self, s):
        self.src = s
        self.ptr = 0
        return self.getString()
