from typing import Optional

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(h), where H is the height of the tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.value

            curr = curr.right


s = Solution()

a = TreeNode(1)
a.right = TreeNode(2)

root = TreeNode(3)
root.left = a
root.right = TreeNode(4)

print(s.kthSmallest(root, 1))


c = TreeNode(2)
c.left = TreeNode(1)

b = TreeNode(3)
b.left = c
b.right = TreeNode(4)

root = TreeNode(5)
root.left = b
root.right = TreeNode(6)

print(s.kthSmallest(root, 3))
