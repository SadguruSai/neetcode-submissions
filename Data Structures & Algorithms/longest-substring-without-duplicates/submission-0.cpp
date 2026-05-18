class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> hash;
        int left=0;
        int right=0;
        int max_len=0;
        while(right<s.length()){
            if(hash.find(s[right])!=hash.end()){
                hash.erase(s[left]);
                left++;
            }
            else{
                hash.insert(s[right]);
                right++;
                int len=right-left;
                max_len=max(max_len,len);
            }
        }
        return max_len;
    }
};
