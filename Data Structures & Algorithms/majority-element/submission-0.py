class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        res=max_count=0
        for i in nums:
            freq[i]+=1
            if freq[i]>max_count:
                max_count=freq[i]
                res=i
        return res