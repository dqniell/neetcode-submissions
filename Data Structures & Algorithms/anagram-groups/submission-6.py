class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping_list = defaultdict(list)
        for word in strs: 
            key = "".join(sorted(word))
            grouping_list[key].append(word)
        return list(grouping_list.values())