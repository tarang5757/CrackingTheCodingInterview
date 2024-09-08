class Solution:
    def maxProfit(self, prices):

        left = 0 #sell
        right = 1 #buy
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

            else:
                left = right
            right += 1

        
        return max_profit



lol = Solution()
arr = [10, 1, 5, 6, 7 ,1]
print(lol.maxProfit(arr))







        