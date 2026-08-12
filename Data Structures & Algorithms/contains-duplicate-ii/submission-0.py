class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #sliding window problem
        #initiate two poniters left and right
        #make a hash that has all the values in the window
        #when window beomes larger than the k then remove the leftmost element from hash and and new from right
        left,right=0,0
        visited=set()
        while(right<len(nums)):
            if nums[right] in visited:
                return True
            visited.add(nums[right])
            if right-left>=k:
                visited.remove(nums[left])
                left+=1
            right+=1
        return False
