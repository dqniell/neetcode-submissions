class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #given a string s, i need to find the length of the longest substring without duplicate characters

        #will this string contain only letters or will it contain whitespace?
        #is there a size limit?
        #if its len 1, i assume that you just return 1? 

        # z x y z x y z -> 
        # |     |

        l = 0
        r = l + 1
        longest = 0
        seen = set()  

        if not s:
            return 0

        if len(s) == 1:
            return 1

        seen.add(s[0])

        while r < len(s): 
            if s[r] not in seen: 
                seen.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else: 
                seen.remove(s[l]) 
                l += 1
        return longest