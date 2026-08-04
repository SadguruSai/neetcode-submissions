class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        curr_val=nums[0]
        for i in nums:
            if i==curr_val:
                count+=1
            elif i!=curr_val and count>0:
                count-=1
            else:
                curr_val=i
        return curr_val