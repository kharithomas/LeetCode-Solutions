from typing import Optional, List
from collections import deque

from helpers.tree import TreeNode


# TC : O(N)
# SC : O(N)


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = deque()
        q = deque([root])
        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.value)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.appendleft(list(level))

        return list(res)


s = Solution()

a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(7)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = a

print(s.levelOrderBottom(root))
