class Solution:
    def kthSmallest(self, root, k):
        data = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            
            data.append(node.val)

            if node.right:
                traverse(node.right)
        
        traverse(root)
        return data[k-1]