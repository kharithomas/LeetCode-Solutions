from typing import List

from collections import deque


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root: TreeNode = None) -> None:
        self.root = root

    def insert(self, root: TreeNode, value: int) -> None:
        if root is None:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def inorder_traversal(self) -> List[int]:
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def preorder_traversal(self) -> List[int]:
        if not self.root:
            return []

        result = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.value)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

        return result

    def postorder_traversal(self) -> List[int]:
        if not self.root:
            return []

        result = []
        stack = []
        curr, prev = self.root, None

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]

            if not curr.right or curr.right == prev:
                stack.pop()
                result.append(curr.val)
                prev = curr
                curr = None
            else:
                curr = curr.right

        return result

    def levelorder_traversal(self) -> List[int]:
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


if __name__ == "__main__":

    values = [7, 3, 10, 1, 5, 9, 12]
    tree = BinaryTree()

    for value in values:
        if tree.root is None:
            tree.root = TreeNode(value)
        else:
            tree.insert(tree.root, value)

    print("In-order Traversal  :", tree.inorder_traversal())
    print("Pre-order Traversal :", tree.preorder_traversal())
    print("Post-order Traversal:", tree.postorder_traversal())
