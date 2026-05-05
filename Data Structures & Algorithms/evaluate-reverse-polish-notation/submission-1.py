class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        total = 0
        for c in tokens:
            if c not in "+-*/":
                stk.append(int(c))
            elif c == "+":
                stk.append(stk.pop() + stk.pop())
            elif c == "-":
                a, b = stk.pop(), stk.pop()
                stk.append(b - a)
            elif c == "*":
                stk.append(stk.pop() * stk.pop())
            elif c == "/":
                a,b = stk.pop(), stk.pop()
                stk.append(int(float(b)/a))
        return stk[0]            