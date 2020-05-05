import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue 
# from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # PLAN
        #looks to see if node value is greater than self.value, is so recurse left
        if value < self.value:
            #if so go left side and check if the left is empty
            if self.left is None:
                #if so the node value then becomes the new value and return it 
                self.left = BinarySearchTree(value)
                return
            else:
                #but if there is a value then inserts the value in the left node
                self.left.insert(value)

        #But if node value is less than or equal to self.value
        if value >= self.value:
            #go right and check if the right side is empty
            if self.right is None:
                #if so node value becomes the new value for the right
                self.right = BinarySearchTree(value)
                return
            else:
                #but if there is a value then it inserts it in the right side
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # PLAN
        # check/compare if the node is empty
        # check/compare if the node value is the same as target search value
            # return true
        # else if target search value is less than the node value (go left ) and if there is node.left  
            # return  the left side contains the target
        # else if target is  greater than the tree value recurse right and if there is node.right 
            # return  the right side contains the target
        ## else return false
        
        if self.value == None:
            return False
        if self.value == target:
            return True
        # elif target < self.value and self.left :
            #  return self.left.contains(target)
        # elif self.right and target > self.value:
        #     return self.right.contains(target)
        elif target < self.value:
            if self.left:
                return self.left.contains(target)   
        elif target > self.value:
            if self.right:
                return self.right.contains(target)   
        # else:
        #     return False

    # Return the maximum value found in the tree
    def get_max(self):
        # PLAN
        # check if there is a value on the right 
            # if so return get max value on right
        # else return node.value

        if self.right:
            return self.right.get_max()
        else:
            return self.value
        

