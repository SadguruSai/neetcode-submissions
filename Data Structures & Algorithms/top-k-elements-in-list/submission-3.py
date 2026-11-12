class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1

        bucket=[[] for _ in range(len(nums)+1)]

        for key,val in freq.items():
            bucket[val].append(key)

        temp=k
        ptr=len(nums)
        while temp>0:
            while len(bucket[ptr])>0 and temp>0:
                last=bucket[ptr].pop()
                ans.append(last)
                temp-=1
            ptr-=1
        return ans
        
            
