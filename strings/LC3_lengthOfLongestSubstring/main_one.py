# Approach 2:
#     n = length(s)
#     longest = 0
#     left = 0
#     right = 0
#     seen = empty set
    
#     while right < n:
#         if s[right] not in seen:
#             add s[right] to seen
#             right = right + 1
#             longest = max(longest, right - left)
#         else:
#             remove s[left] from seen
#             left = left + 1
    
#     return longest


class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        longest = 0
        left = 0
        right = 0
        seen = set()
        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right +=1
                longest = max(longest, right - left)
            else:
                seen.remove(s[left])
                left +=1
        return longest

