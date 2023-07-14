class Solution:
    def isValid(self, s):
        stack = []
        pairs_hashmap = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in pairs_hashmap:
                stack.append(char)
            elif len(stack) == 0 or pairs_hashmap[stack.pop()] != char:
                return False
        return len(stack) == 0
                

