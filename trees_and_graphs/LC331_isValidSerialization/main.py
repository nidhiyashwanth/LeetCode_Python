class Solution:
    def isValidSerialization(self, preorder):
        slots = 1
        p = preorder.split(',')

        for node in p:
            slots -= 1
            if slots < 0:
                return False
            if node != "#":
                slots += 2
        return slots == 0