class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root