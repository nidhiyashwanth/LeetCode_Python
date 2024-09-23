class Solution:
    def isValidBST(self, root):
        validity = True

        def helper(node, minimum, maximum):
            nonlocal validity
            if not node or not validity:
                return
            
            if (minimum != None and node.val <= minimum)  or (maximum != None and node.val >= maximum):
                validity = False
                return
            
            helper(node.left, minimum, node.val)
            helper(node.right, node.val, maximum)

        helper(root, None, None)
        return validity