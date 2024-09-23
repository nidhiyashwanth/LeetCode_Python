class Solution:
    def maxDepth(self, root):
        max_depth = 0

        def dive(node, current_depth):
            nonlocal max_depth
            if not node:
                max_depth = max(current_depth - 1, max_depth)
                return
            
            dive(node.left, current_depth + 1)
            dive(node.right, current_depth + 1)
        dive(root, 1)
        return max_depth