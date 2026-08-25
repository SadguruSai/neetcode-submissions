class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=nums[0]
        curr_sum=nums[0]

        left,right=1,1
        while(right<len(nums)):
            if curr_sum<0:
                curr_sum=nums[right]
                left=right
            else:
                curr_sum+=nums[right]
            right+=1
            max_sub=max(max_sub,curr_sum)

        return max_sub