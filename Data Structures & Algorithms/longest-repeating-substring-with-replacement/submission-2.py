class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0 
        max_frequency = 0 
        counts = {}

        for r in range(len(s)): 
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_frequency = max(max_frequency, counts[s[r]])
            window_length = r - l + 1

            while window_length - max_frequency > k: 
                counts[s[l]] -= 1
                l += 1
                window_length = r - l + 1

            longest = max(longest, window_length)
        return longest
                
                