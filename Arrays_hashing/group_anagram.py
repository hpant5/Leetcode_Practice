#problem stat Given an array of strings strs, group all anagrams together into sublists.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_str = tuple(sorted(s))
            anagrams[sorted_str].append(s)
        return list(anagrams.values())