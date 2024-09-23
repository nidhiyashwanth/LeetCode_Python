class Solution:
    def invertTree(self, root):
        self.helper(root)
        return root
    
    def helper(self, node):
        if not node:
            return
        
        temp = node.left
        node.left = node.right
        node.right = temp

        self.helper(node.left)
        self.helper(node.right)