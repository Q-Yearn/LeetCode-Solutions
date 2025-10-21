class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        string = {}
        string["2"] = "abc"
        string["3"] = "def"
        string["4"] = "ghi"
        string["5"] = "jkl"
        string["6"] = "mno"
        string["7"] = "pqrs" 
        string["8"] = "tuv"
        string["9"] = "wxyz"
        result = []
        def DFS(cur, path):
            # python3中才有
            # 也可以使用self, 这里直接使用函数传递
            # nonlocal path  # <-- 现在这行代码是有效的了

            if cur == len(digits):
                result.append(path)
                return

            for c in string[digits[cur]]:
                DFS(cur + 1, path+c)
        
        DFS(0, "")
        return result