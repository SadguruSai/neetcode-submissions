class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        n=len(temperatures)
        ans=[0]*n
        for i in range(0,n):
            while(st and temperatures[i]>temperatures[st[-1]]):
                idx=st.pop()
                ans[idx]=i-idx
            st.append(i)
        return ans
