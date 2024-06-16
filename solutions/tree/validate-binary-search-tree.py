from typing import Optional

from helpers.tree import TreeNode


# TC : O(N)
# SC : O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()

            # check node is within boundary
            if node.value <= low or node.value >= high:
                return False

            if node.left:
                stack.append((node.left, low, node.value))

            if node.right:
                stack.append((node.right, node.value, high))

        return True


s = Solution()

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(s.isValidBST(root))


b = TreeNode(4)
b.left = TreeNode(3)
b.right = TreeNode(6)

root = TreeNode(5)
root.left = TreeNode(1)
root.right = b

print(s.isValidBST(root))
