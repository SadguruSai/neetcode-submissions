class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo,hi=0,len(nums)-1
        curr=0
        while(curr<=hi):
            if(nums[curr]==0):
                nums[lo], nums[curr] = nums[curr], nums[lo]
                lo+=1
                curr+=1
            elif(nums[curr]==2):
                nums[hi], nums[curr] = nums[curr], nums[hi]
                hi-=1
            else:
                curr+=1

        