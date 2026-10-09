class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()

        for i in range(len(s)): 
            while s[i] in sett: 
                sett.remove(s[l])
                l += 1
            sett.add(s[i])
            longest = max(longest, i - l + 1)
        
        return longest
        