class TrieNode{
public:
    unordered_map<char,TrieNode*> children;
    bool isend=false;
};
class PrefixTree {
    TrieNode* root;
public:
    PrefixTree() {
        root=new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* cur=root;
        for(auto& c:word){
            if(cur->children.find(c)==cur->children.end()){
                cur->children[c]=new TrieNode();
            }
            cur=cur->children[c];   
        }
        cur->isend=true;
    }
    
    bool search(string word) {
        TrieNode* cur=root;
        for(auto& c:word){
            if(cur->children.find(c)==cur->children.end()){
                return false;
            }
            cur=cur->children[c];
        }
        return cur->isend;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur=root;
        for(auto& c:prefix){
            if(cur->children.find(c)==cur->children.end()){
                return false;
            }
            cur=cur->children[c];
        }
        return true;
    }
};
