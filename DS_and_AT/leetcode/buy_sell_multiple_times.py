class Solution:
    def maxProfit(self, prices) -> int:
        
        buy = 1
        profit = 0
        curr = 0
        stock = 0
        while curr < len(prices) -1:
            if buy:
                if curr == len(prices)-1:
                    break
                elif prices[curr] < prices[curr+1]:
                    buy = 0
                    stock = prices[curr]
                curr +=1
            else:
                if curr == len(prices) - 1:
                    if prices[curr] > stock:
                        profit += prices[curr] - stock
                    break
                elif  prices[curr] > prices[curr+1]:
                    buy =1
                    profit += prices[curr] - stock
                    curr +=1
        return profit