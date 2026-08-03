class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            size = len(string)
            encoded += (str(size) + '#' + string)
        return encoded

    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            length_of_string = int(s[i:j])
            sol.append(s[j+1: j + 1 + length_of_string])
            i = j + 1 + length_of_string
        return sol

#       5#Hello5#World