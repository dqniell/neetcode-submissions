class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLongest = 0
        
        for l in range(len(s)): 
            sett = set()
            longest = 0
            r = l
            while r < len(s) and s[r] not in sett: 
                sett.add(s[r])
                longest += 1
                r += 1
            maxLongest = max(longest, maxLongest)
        return maxLongest
