class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 or len(prices) == 0:
            return 0
        profit = 0
        lowest = [0]*len(prices)
        profitToday = []
        lowest[0] = prices [0]       
        for i in range(1, len(prices)):
            lowest[i] = min(prices[i], lowest [i-1])
            profitToday.append(max(0, (prices[i]-lowest[i])))
        return max(profitToday)
            