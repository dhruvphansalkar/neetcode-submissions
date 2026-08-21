class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operands = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in operands:
                num2 = st.pop()
                if token == '+':
                    st[-1] += num2
                if token == '-':
                    st[-1] -= num2
                if token == '*':
                    st[-1] *= num2
                if token == '/':
                    st[-1] = int(st[-1]/num2)
            else:
                st.append(int(token))    
        return st[0]