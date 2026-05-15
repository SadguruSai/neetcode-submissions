class Solution {
private: 
string makeKey(string& s){
    int freq[26]={0};
    for(char c:s){
        freq[c-'a']++;
    }

    string key="";

    for(int i=0;i<26;i++){
        key+=to_string(freq[i]);
        key+="#";
    }
    return key;
}
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hash;
        vector<vector<string>> ans;

        for(string x:strs){
            string y=makeKey(x);
            hash[y].push_back(x);
        }
        for(auto x:hash){
            ans.push_back(x.second);
        }
        return ans;
    }
};
