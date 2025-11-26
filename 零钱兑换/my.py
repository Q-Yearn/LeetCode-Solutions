# 超时了  不同层级可能出现重复的遍历
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        count = 0
        queue = [amount]
        while queue:
            count += 1
            new_queue = set()
            for num in queue:
                for coin in coins:
                    if coin <= num:
                        if num - coin == 0:
                            return count
                        new_queue.add(num-coin)
            queue = new_queue
        return -1

# 或者使用集合存储遍历过的金额
# 使用了visited保证同一层也不会有重复 可以直接使用list当queue
# 列表的append比集合的add快
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        visited = [0] * (amount+1)
        count = 0
        queue = [amount]
        while queue:
            count += 1
            new_queue = set()
            for num in queue:
                for coin in coins:
                    if coin <= num:
                        if num - coin == 0:
                            return count
                        if visited[num-coin] == 0:
                            new_queue.add(num-coin)
                            visited[num-coin] = 1
            queue = new_queue
        return -1

