from typing import Optional, List
from collections import deque

from helpers.tree import TreeNode


# TC : O(NlogN)
# SC : O(N)

class Solution:
    def topView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        offsets = {}
        q = deque([(root, 0)])

        while q:
            for _ in range(len(q)):
                node, offset = q.popleft()

                if offset not in offsets:
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
a.right = TreeNode(4)

b = TreeNode(5)
b.left = a
b.right = TreeNode(6)

c = TreeNode(2)
c.right = b

root = TreeNode(1)
root.right = c

print(s.topView(root))
