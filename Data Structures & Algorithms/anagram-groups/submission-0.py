class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listt = {}
        
        for word in strs: 
            sorted_word = ''.join(sorted(word))
            
            if sorted_word in listt: 
                listt[sorted_word].append(word)
            else: 
                listt[sorted_word] = [word]
        
        return list(listt.values())