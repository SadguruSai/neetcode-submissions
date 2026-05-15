class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hash;
        for(auto i:nums){
            if(hash.find(i)!=hash.end()){
                return true;
            }
            hash.insert(i);
        }
        return false;
    }
};