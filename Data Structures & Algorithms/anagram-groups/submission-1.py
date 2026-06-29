class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mapp = {}
        for word in strs: 
            key = tuple(sorted(word))
            if key not in mapp: 
                mapp[key] = []
            mapp[key].append(word)
        
        for pair in mapp: 
            result.append(mapp[pair])
        return result