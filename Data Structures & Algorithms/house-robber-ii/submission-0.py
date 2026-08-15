class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_helper(i,j):
            if j-i==1:
                return nums[i]
            pre_pre=nums[i]
            pre=max(nums[i],nums[i+1])
            for k in range (i+2,j):
                ans=max(nums[k]+pre_pre,pre)
                pre_pre = pre
                pre = ans
            return pre
        one=rob_helper(0,len(nums)-1)
        two=rob_helper(1,len(nums))
        return max(one,two)
        