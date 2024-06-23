from typing import Optional
from collections import deque

from helpers.tree import TreeNode


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([(root, None)])
        parents = {}

        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()

                if node.value == x or node.value == y:
                    parents[node.value] = parent

                if node.left:
                    q.append((node.left, node))

                if node.right:
                    q.append((node.right, node))

            if x in parents and y in parents:
                return parents[x] != parents[y]

            if x in parents or y in parents:
                return False


s = Solution()

a = TreeNode(2)
a.left = TreeNode(4)

b = TreeNode(3)

root = TreeNode(1)
root.left = a
root.right = b

print(s.isCousins(root,  4, 3))

a = TreeNode(2)
a.right = TreeNode(4)

b = TreeNode(3)
b.right = TreeNode(5)

root = TreeNode(1)
root.left = a
root.right = b

print(s.isCousins(root, 5, 4))
