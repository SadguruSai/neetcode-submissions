class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        max_diff=0
        while right<len(prices):
            if prices[left]>prices[right]:
                left=right
            diff=prices[right]-prices[left]
            max_diff=max(diff,max_diff)
            right+=1
        return max_diff
            