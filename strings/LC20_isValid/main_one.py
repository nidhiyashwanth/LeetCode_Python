# Pseudocode
    # Initialize an empty stack to store opening brackets.
    # Iterate through each character c in the string:
    #     If c is an opening bracket ((, {, [), add it to the stack.
    #     If c is a closing bracket (), }, ]), perform the following checks:
    #         If the stack is empty, there are no opening brackets to match the current closing bracket, so the string is not valid. Return False.
    #         If the top of the stack matches the current closing bracket, remove the top element from the stack (matching opening bracket found).
    #         If the top of the stack does not match the current closing bracket, the string is not valid. Return False.
    # After iterating through the string, if the stack is empty, it means all opening brackets have been matched with closing brackets. Return True.
    # If the stack is not empty, there are unmatched opening brackets remaining. Return False.
class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack:
                return False
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return not stack