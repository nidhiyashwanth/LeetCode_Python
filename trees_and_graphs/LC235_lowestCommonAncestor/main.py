class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current_node = root

        while current_node:
            if current_node.val < p.val and current_node.val < q.val:
                current_node = current_node.right
            elif current_node.val > p.val and current_node.val > q.val:
                current_node = current_node.left
            else:
                return current_node
            