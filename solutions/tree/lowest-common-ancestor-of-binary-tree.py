from helpers.tree import TreeNode

# TC : O(N)
# SC : O(h), as h can be n in the worst case


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.value == p.value or root.value == q.value:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # root node is the LCA
        if left and right:
            return root

        # LCA came from a child node
        return left or right


s = Solution()

a = TreeNode(2)
a.left = TreeNode(7)
a.right = TreeNode(4)

b = TreeNode(1)
b.left = TreeNode(0)
b.right = TreeNode(8)

c = TreeNode(5)
c.left = TreeNode(6)
c.right = a

root = TreeNode(3)
root.left = c
root.right = b

print(s.lowestCommonAncestor(root, TreeNode(5), TreeNode(1)).value)
print(s.lowestCommonAncestor(root, TreeNode(5), TreeNode(4)).value)
