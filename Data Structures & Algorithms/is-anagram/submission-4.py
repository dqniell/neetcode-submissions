class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for i in range(len(s)): 
            if s[i] not in s_count: 
                s_count[s[i]] = 1
            elif s[i] in s_count: 
                s_count[s[i]] += 1
        print(s_count)
        
        for i in range(len(t)): 
            if t[i] not in t_count: 
                t_count[t[i]] = 1
            elif t[i] in t_count: 
                t_count[t[i]] += 1
        print(t_count)
        
        return (s_count) == (t_count)