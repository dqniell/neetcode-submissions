class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0 
        maxLength = 0

        for r in range(len(s)): 
            while s[r] in sett: 
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            maxLength = max(r - l + 1, maxLength)
        
        return maxLength

