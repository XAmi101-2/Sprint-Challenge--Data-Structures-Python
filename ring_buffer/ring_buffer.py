from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # # plan
        # check if the length is less than the cap
        #     if it is add item to the tail and return
        # check if current is empty/with no value
        #      set it to head
        # then assign the current value to the item
        # then add the next value

        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            return
        if self.current == None:
            self.current = self.storage.head
        self.current.value = item
        self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        #while current node is not empty:
        while current_node:
            #append/add it
            list_buffer_contents.append(current_node.value)
            #set current node to next value
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------
 

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
