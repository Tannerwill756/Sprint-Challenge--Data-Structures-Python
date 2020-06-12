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

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    def iter_depth_first_for_each(self, fn):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            fn(self.value)

    def iter_breadth_first_search(self, fn):
        # breadth first traversal follows FIFO ordering of its nodes
        # init a deque
        q = deque()
        # add the first node to our q
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        q = deque()

        q.append(self)

        while len(q) > 0:

            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(node)

        if self.right:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if self.left:
            self.left.post_order_dft(node)

        if self.right:
            self.right.post_order_dft(node)
        print(self.value)
