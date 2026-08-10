class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        size_price=len(prices)
        size_dis=len(discounts)
        ans=0
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        for i in range(size_price):
            if(i<size_dis):
                ans+=prices[i] * (100 - discounts[i]) / 100
            else:
                ans+=prices[i]
        return ans
