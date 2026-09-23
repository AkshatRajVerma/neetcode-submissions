class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in groups:
                groups[key].append(i)
            else:
                groups[key] = [i]
        return list(groups.values())