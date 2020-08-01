class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        self.prev = prev
        self.node = node
        # define current node
        current = node

        # while the head is not yet none
        while(current is not None): 
            # set the next node to the current head node
            head_node = current.next_node

            # set the next node to the previous node which is provided
            current.next_node = prev 

            # the previous node is the current node
            prev = current 

            # the current node is the next node
            current = head_node

            # continou this process until the current node, aka the head is None. 
        self.head = prev 