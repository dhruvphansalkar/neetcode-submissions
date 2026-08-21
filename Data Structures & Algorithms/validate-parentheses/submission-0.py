class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(['(', '{', '['])
        m = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        st = []
        for b in s:
            if b in opening:
                st.append(b)
            else:
                if st and st[-1] == m[b]:
                    st.pop()
                else:
                    return False
        return len(st) == 0

        