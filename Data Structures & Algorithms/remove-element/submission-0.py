class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left,right=0,len(nums)-1
        def swap(l,r):
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
        while(left<=right):
            if(nums[left]==val):
                swap(left,right)
                right-=1
            else:
                left+=1
        return left