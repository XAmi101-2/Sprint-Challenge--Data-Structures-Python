class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # stores the previous and next values, and switches them as it iterates over the linked list, reversing the pointers
        # Create the values
        prev = None
        nxt = None
        curr = self.head

        # PLAN
        #while current node is not none/empty
            #store the next node in nxt
            # nxt = curr.get_next()
            #point the next node to the previous node
            # curr.set_next(prev)
            #moves everything over one to start the next loop by setting prev node
            #sets current node value into the next node
        #resets the list to point to a new head
# loops hrough until node is none

        while curr is not None:
            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt
        self.head = prev
        


