class Solution:

    def IsOperand(self,string)->bool:
        if(string=="+" or string=="-" or string=="/" or string=="*"):
            return True
        return False

    def Calculate(self,a,b,op)->int:
        if op=="+": return a+b
        if op=="-": return a-b
        if op=="/": return int(a/b)
        if op=="*": return a*b
    
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        i=0
        while(i<len(tokens)):
            if(self.IsOperand(tokens[i])):
                b=st.pop()
                a=st.pop()
                st.append(self.Calculate(a,b,tokens[i]))
            else:
                st.append(int(tokens[i]))
            i+=1
        return int(st.pop())   