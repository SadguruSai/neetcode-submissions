class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        left=0
        mid=left+1
        right=len(nums)-1
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            mid,right=i+1,len(nums)-1
            while mid<right:
                curr_sum=nums[i]+nums[mid]+nums[right]
                if curr_sum==0:
                    ans.append([nums[i],nums[mid],nums[right]])
                    mid+=1
                    right-=1

                    while mid<right and nums[mid]==nums[mid-1]:
                        mid+=1
                    while mid<right and nums[right]==nums[right+1]:
                        right-=1

                elif curr_sum<0:
                    mid+=1
                else:
                    right-=1
        return ans
