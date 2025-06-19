#Question: You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#First Solution, 29ms, beats 87.84% of submissions

class Solution:
  
    def maxProfit(self, prices: List[int]) -> int:
    
        current_min = 10001
        current_profit = 0

        for i in prices:

            if i < current_min:
                current_min = i
            else:
                if i - current_min > current_profit:
                    current_profit = i - current_min
                else:
                    pass
        
        return current_profit
