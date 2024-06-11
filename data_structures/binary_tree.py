from typing import List


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
        stack1, stack2 = [self.root]

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)

            if current.right:
                stack1.append(current.right)

        while stack2:
            current = stack2.pop()
            result.append(current.value)

        return result

    def levelorder_traversal(self) -> List[int]:
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
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
