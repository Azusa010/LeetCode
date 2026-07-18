class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        table = dict()
        for word in strs:
            key = tuple(sorted(word))
            if key not in table:
                table[key] = []
            table[key].append(word)
        return list(table.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
