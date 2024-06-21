

from typing import Optional, List
from collections import deque

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                # last node in level
                if i == (level_size - 1):
                    res.append(node.value)

        return res


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

print(s.rightSideView(root))
