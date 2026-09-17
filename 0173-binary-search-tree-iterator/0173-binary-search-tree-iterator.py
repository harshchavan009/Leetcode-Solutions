class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()

        # All nodes in the right subtree come after this node
        if node.right:
            self.push_left(node.right)

        return node.val

    def hasNext(self):
        return len(self.stack) > 0