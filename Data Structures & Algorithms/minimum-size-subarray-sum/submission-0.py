class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window problem
        #keep adding right until sum becomes greater than given target
        #once become greater remove from left keep ans=min(ans,new)
        #keep doing until found min
        left,right=0,0
        ans=float('inf')
        curr_sum=0
        while(right<len(nums)):
            curr_sum+=nums[right]
            while(curr_sum>=target):
                ans=min(ans,right-left+1)
                curr_sum -= nums[left]
                left+=1
            right+=1
        if(ans==float('inf')):
            return 0
        else:
            return ans
