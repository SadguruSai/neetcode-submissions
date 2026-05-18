class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> hash;
        int left=0;
        int max_len=0;
        for(int right=0;right<s.length();right++){
            while(hash.find(s[right])!=hash.end()){
                hash.erase(s[left]);
                left++;
            }
            hash.insert(s[right]);
            max_len=max(max_len,right-left+1);
        }
        return max_len;
    }
};
