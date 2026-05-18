class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> hash;
        int left=0;
        int right=0;
        int len=0;
        int max_len=0;
        while(right<s.length()){
            while(hash.find(s[right])!=hash.end()){
                hash.erase(s[left]);
                left++;
            }
                hash.insert(s[right]);
                len=right-left+1;
                max_len=max(max_len,len);
                right++;
        }
        return max_len;
    }
};
