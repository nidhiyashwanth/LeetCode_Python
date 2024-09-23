class Solution:
    def isSameTree(self, p, q):
        same_tree = True
        def check_same_node(p,q):
            nonlocal same_tree
            if (not p and not q) or not same_tree:
                return
            elif not p or not q:
                same_tree = False
                return
            elif p.val != q.val:
                same_tree = False
                return
            
            check_same_node(p.left, q.left)
            check_same_node(p.right, q.right)
        check_same_node(p,q)
        return same_tree