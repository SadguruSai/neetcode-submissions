class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        dic=defaultdict(list)
        for node,par in enumerate(parent):
            if[par]!=-1:
                dic[par].append(node)
        que=deque()
        que.append(0)
        d=1
        res=0
        while que:
            for _ in range(len(que)):
                node=que.popleft()
                res+=nums[node]*(-d+1)
                for child in dic[node]:
                    que.append(child)
            d+=1
        return res+((d-1)*sum(nums))

        
