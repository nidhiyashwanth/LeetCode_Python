class Solution:
    def isValidSerialization(self, preorder):
        slots = 1

        for i in range(len(preorder)):
            char = preorder[i]

            if char == ',':
                slots -= 1

                if slots < 0:
                    return False
                
                prevChar = preorder[i - 1]
                if prevChar != '#':
                    slots += 2
        
        if preorder[-1] == '#':
            slots -= 1
        else:
            slots +=1
        return slots == 0