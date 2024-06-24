from typing import Optional, List
from collections import deque

from helpers.tree import TreeNode


# TC : O(NlogN)
# SC : O(N)

class Solution:
    def bottomView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        offsets = {}
        q = deque([(root, 0)])

        while q:
            for _ in range(len(q)):
                node, offset = q.popleft()
                offsets[offset] = node.value

                if node.left:
                    q.append((node.left, offset - 1))

                if node.right:
                    q.append((node.right, offset + 1))

        # Sorting the keys and creating the top view list
        res = [offsets[key] for key in sorted(offsets)]

        return res


s = Solution()

a = TreeNode(3)
a.left = TreeNode(10)
a.right = TreeNode(14)

b = TreeNode(22)
b.right = TreeNode(25)

c = TreeNode(8)
c.left = TreeNode(5)
c.right = a

root = TreeNode(20)
root.left = c
root.right = b

print(s.bottomView(root))
