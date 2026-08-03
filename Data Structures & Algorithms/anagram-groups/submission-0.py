class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol_dict = {}
        for word in strs:
            base_key = [0] * 26
            for c in word:
                base_key[ord(c) - ord('a')] += 1
            key = tuple(base_key)
            updatde_array = sol_dict.get(key, [])
            updatde_array.append(word)
            sol_dict[key] = updatde_array
        
        return [grouped_anagram for grouped_anagram in sol_dict.values()]

        