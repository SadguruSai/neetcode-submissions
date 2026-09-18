class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        ans=[]
        def retKey(stri):
            arr=[0]*26
            for c in stri:
                arr[ord(c)-ord('a')]+=1
            return tuple(arr)
        for s in strs:
            key=retKey(s)
            if key not in hash_map:
                hash_map[key]=[]
            hash_map[key].append(s)
        
        return list(hash_map.values())

        
