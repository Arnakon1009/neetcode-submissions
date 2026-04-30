class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')' : '(', '}' : '{', ']':'['}
        stk = []

        for i in range(len(s)):
            if s[i] in "{[(":
                stk.append(s[i])
            else:
                if not stk: return False
                if stk.pop() != mapping[s[i]]: return False
        return True if not stk else False
