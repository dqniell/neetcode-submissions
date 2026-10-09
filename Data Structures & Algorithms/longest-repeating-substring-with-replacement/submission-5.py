class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #given a window of characters, what is the min number of replacements needed to make it all one char
        #so i need to replace everything that is not the most frequent character

        #sliding window --> expand right as long as the window is valid
        #once invalid, shrink from left until its valid again
        #track the longest valid window
        #valid = window size - max freq <= k
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res