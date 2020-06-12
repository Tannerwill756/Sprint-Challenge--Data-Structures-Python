from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # 1. check if there is no root
        if self is None:
            # if there isn't, create the node and park it there
            self = BSTNode(value)
        # 2. otherwise, there is a root
        else:
            # compare teh value to the root's value to determine which direction we go in
            # if the value < roots value
            if value < self.value:
                # go left
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            # if the value > roots value
            else:
                # go right
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
