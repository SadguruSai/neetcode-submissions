class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int i=0;
        while(i<tokens.size()){
            if(tokens[i]!= "+" && tokens[i]!= "-" && tokens[i]!= "*" && tokens[i]!= "/"){
                st.push(stoi(tokens[i]));
                i++;
            }
            else{
                int two=st.top();
                st.pop();
                int one=st.top();
                st.pop();
                int three=0;
                if(tokens[i]=="+"){
                    three=one+two;
                    st.push(three);
                }
                else if(tokens[i]=="-"){
                    three=one-two;
                    st.push(three);
                }
                else if(tokens[i]=="*"){
                    three=one*two;
                    st.push(three);
                }
                else if(tokens[i]=="/"){
                    three=one/two;
                    st.push(three);
                }
                i++;
            }
        }
        return st.top();
    }
};
