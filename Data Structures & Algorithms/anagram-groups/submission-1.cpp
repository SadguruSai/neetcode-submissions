class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hash;
        vector<vector<string>> ans;

        for(string x:strs){
            string temp=x;
            sort(x.begin(),x.end());
            hash[x].push_back(temp);
        }
        for(auto x:hash){
            ans.push_back(x.second);
        }
        return ans;
    }
};
