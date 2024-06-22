from typing import Optional, List
from collections import deque

from helpers.tree import TreeNode

# TC : O(N)
# SC : O(N)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            level = deque()

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(list(level))

        return res


s = Solution()

a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(7)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = a

print(s.levelOrder(root))
