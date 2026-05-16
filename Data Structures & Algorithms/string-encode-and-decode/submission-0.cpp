class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty()) return "";
        string encode="";
        for(string s:strs){
            encode+=to_string(s.length());
            encode+=',';
        }
        encode+='#';
        for(string s:strs){
            encode+=s;
        }
        return encode;
    }

    vector<string> decode(string s) {
        if(s.empty()) return {};
        vector<int> size;
        vector<string> ans;
        int i=0;
        while(s[i]!='#'){
            string cur="";
            while( s[i]!=','){
                cur+=s[i];
                i++;
            }
            size.push_back(stoi(cur));
            i++;
        }
        i++;
        for (int k:size){
            ans.push_back(s.substr(i,k));
            i+=k;
        }

    return ans;

    }
};
