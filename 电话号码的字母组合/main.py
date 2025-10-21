# 这些代码都没有考虑digits里有1的情况  
# 如果有1  string可以使用get方法找到key
# DFS遇到1的时候需要直接进行DFS跳过path.append
# DFS如果只遇到一个1的情况  直接返回空列表就行  注意[""]这种
# 迭代遇到1的时候直接result=reuslt即可
# 优化DFS
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        string = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        path = []
        def DFS(cur):
            if cur == len(digits):
                result.append("".join(path))
                return

            for c in string[digits[cur]]:
                path.append(c)
                DFS(cur + 1)
                path.pop()
        
        DFS(0)
        return result


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        string = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = string[digits[0]]
        if len(digits) == 1:
            return result
        for i in range(1, len(digits)):
            tmp = []
            for c in result:
                for s in string[digits[i]]:
                    tmp.append(c+s)
            result = tmp
        return result