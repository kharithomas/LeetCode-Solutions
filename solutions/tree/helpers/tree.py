from typing import Optional

from collections import deque


class TreeNode:
    """A single node of a Tree"""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def print_tree(root: Optional[TreeNode]) -> None:
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=", ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
