from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = tuple(sorted(Counter(word).items()))  # make Counter hashable
            result[count].append(word)

        return list(result.values())