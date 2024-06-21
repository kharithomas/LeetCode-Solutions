from typing import Optional, List
from collections import deque

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])
        flip = False

        while q:
            level_size = len(q)
            level = deque()

            for _ in range(level_size):
                node = q.popleft()
                if flip:
                    level.appendleft(node.value)
                else:
                    level.append(node.value)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(list(level))
            flip = not flip

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

print(s.zigzagLevelOrder(root))
