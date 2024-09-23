class Solution:
    def levelOrder(self, root):
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, node, depth, res):
        if not node:
            return
        if len(res) <= depth:
            res.append([])
        res[depth].append(node.val)
        self.helper(node.left, depth + 1, res)
        self.helper(node.right, depth + 1, res)