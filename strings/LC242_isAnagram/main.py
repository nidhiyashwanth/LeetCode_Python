class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_char_counts = {}
        for s_char in s:
            if s_char not in s_char_counts:
                s_char_counts[s_char] = 1
            else:
                s_char_counts[s_char] +=1
            
        for t_char in t:
            if t_char not in s_char_counts or s_char_counts[t_char] == 0:
                return False
            else:
                s_char_counts[t_char] -= 1
        return True
