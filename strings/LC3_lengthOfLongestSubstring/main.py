# Brute force will have time complexity of n^3 which is not ideal

# Approach to solve it in linear time:
    # Sliding Window Approach
        # SW (Sliding Window) will represent the current substring of non repeating characters we are on
        # We will not be working with sliding window of fixed size, the window will grow and shrink in size as we iterate through string.
        # Current index and value in loop will always be END of the SW. As end of window increases, we conditionally increase start of window.
    # Pseudo code:
        # Create an empty hashMap(key/val -> Character/index)
        # Create start and end max variable, set both with initial values of zero
        # Loop through input string:
        #     if current character in HashMap & has index >= Start
        #         set start to index for character found in HashMap + 1
        #     set key / value pair on HashMap to be current character or current index
        #     If length of current window is greater than max:
        #         Set max to the length of current window
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        max_length = 0
        window_start = 0
        
        for i in range(len(s)):
            end_char = s[i]
            if end_char in char_map and char_map[end_char] >= window_start:
                window_start = char_map[end_char] +1
            char_map[end_char] = i
            max_length = max(max_length, i - window_start + 1)
        return max_length