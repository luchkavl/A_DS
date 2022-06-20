from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with that value already exists.')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        raise LookupError(f"A node with value {value} was not found.")

    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    def preorder(self):
        self._preorder_recursive(self.head)

    def _preorder_recursive(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._preorder_recursive(current_node.left)
        self._preorder_recursive(current_node.right)

    def find_parent(self, value: int) -> Node:
        child = value
        if self.head and self.head.value == child:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and child == current_node.left.value) or \
                    (current_node.right and child == current_node.right.value):
                return current_node
            elif child < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        raise LookupError(f"A node with value {value} was not found.")

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:
            # we have 2 children
            most_right = self.find_rightmost(to_delete.left)
            most_right_parent = self.find_parent(most_right.value)

            if most_right_parent != to_delete:
                most_right_parent.right = most_right.left
                most_right.left = to_delete.left
            most_right.right = to_delete.right

            if to_delete == to_delete_parent.left:
                to_delete_parent.left = most_right
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = most_right
            else:
                self.head = most_right

        elif to_delete.left or to_delete.right:
            # only 1 child
            if to_delete_parent.left == to_delete:
                to_delete_parent.left = to_delete.left or to_delete.right
            elif to_delete_parent.right == to_delete:
                to_delete_parent.right = to_delete.left or to_delete.right
            else:
                self.head = to_delete.left or to_delete.right
        else:
            # no children
            if to_delete_parent.left == to_delete:
                to_delete_parent.left = None
            elif to_delete_parent.right == to_delete:
                to_delete_parent.right = None
            else:
                self.head = None
