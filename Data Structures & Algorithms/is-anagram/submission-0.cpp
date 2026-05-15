class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()){
            return false;
        }
        unordered_map<int,int> hash;
        for(auto i:s){
            hash[i]++;
        }
        for(auto i:t){
            if(hash[i]==0){
                return false;
            }
            hash[i]--;
        }
        return true;
    }
};
