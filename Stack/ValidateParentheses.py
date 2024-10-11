# problem Statement :You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        di = {')':'(','}':'{',']':'['}
        for i in s:
            if i in di:
                if st and st[-1] == di[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return True if not st else False
