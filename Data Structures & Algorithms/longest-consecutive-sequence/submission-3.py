class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash1=defaultdict(int)
        longest=0
        if len(nums)<=1:
            return len(nums)
        for i in range(len(nums)):
            hash1[nums[i]]=i
        for i in nums:
            if i-1 not in hash1:
                start=i
                length=1
                while(i+length) in hash1:
                    length+=1
                longest=max(length,longest)
        return longest