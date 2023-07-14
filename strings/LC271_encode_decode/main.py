# Design an algorithm to encode a list of strings to a string. The
# encoded string is then sent over the network and is decoded back to
# the original list of strings.

# Example
# encoded_string = encode(['kevin', 'is', 'great'])
#                  "5/kevin2/is5/great"

# decoded_array = decode("5/kevin2/is5/great")
#                 ['kevin', 'is', 'great']

# Notes
# - Do not use class member/global/static variables to store states. Your
#   encode and decode should be stateless
# - Do not use an library method such as eval or serialize methods. You
#   must implement your OWN encode and decode algorithm


class Solution:
    def encode(self, strs):
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length) + "/" + word
        return encoded

        # ChatGPT Answer
        # encoded = ""
        # for s in strs:
        #     encoded += str(len(s)) + "/" + s
        
        # return encoded

    def decode(self, str):  
        pos = 0
        decoded = []
        while pos < len(str):
            slash_pos = str.index("/", pos)
            length = int(str[slash_pos - 1])
            pos = slash_pos + 1
            decoded.append(str[pos: pos + length] )
            pos += length
        return decoded


        # CHATGPT Answer:

        # decoded = []
        # i = 0
        # while i < len(s):
        #     slash_index = s.find("/", i)
        #     size = int(s[i:slash_index])
        #     i = slash_index + size + 1
        #     decoded.append(s[slash_index+1:i])
        
        # return decoded
    
    # Time complexity = O(n)
    # Space Complexity = O(1)
    