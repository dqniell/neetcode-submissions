class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listt = {}
        
        #for each word, sort the word -> since anagrams will have the same sort
        for word in strs: 
            sorted_word = ''.join(sorted(word))

            #if the sorted word is in the map, then 
            #it means we already have a list to return, so we just append it
            if sorted_word in listt: 
                listt[sorted_word].append(word)
            #if not, we need to add it to the map
            else: 
                listt[sorted_word] = [word]
        
        #just returning the values, since it can be in any order
        return list(listt.values())