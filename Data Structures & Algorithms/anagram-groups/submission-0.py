class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where key = sorted word, value = list of anagrams
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the word to create a key and convert to tuple (hashable)
            sorted_word = tuple(sorted(word))
            anagram_map[sorted_word].append(word)

        # Return all grouped anagrams as a list of lists
        return list(anagram_map.values())