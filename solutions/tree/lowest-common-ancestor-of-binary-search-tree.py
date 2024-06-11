from helpers.tree import TreeNode

# TC : O(N), where N is the total number of nodes in tree
# SC : O(1)


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        curr = root

        while curr:
            if p.value > curr.value and q.value > curr.value:
                curr = curr.right
            elif p.value < curr.value and q.value < curr.value:
                curr = curr.left
            else:
                return curr


s = Solution()


a = TreeNode(8)
a.left = TreeNode(7)
a.right = TreeNode(9)

c = TreeNode(4)
c.left = TreeNode(3)
c.right = TreeNode(5)

b = TreeNode(2)
b.left = TreeNode(0)
b.right = c

root = TreeNode(6)
root.left = b
root.right = a

print(s.lowestCommonAncestor(root, b, a).value)
print(s.lowestCommonAncestor(root, b, c).value)
