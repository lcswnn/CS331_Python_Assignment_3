# CS331 Assignment 3, 09/23/2022

# In this assignment, you are asked to implement methods in the LinkedList class following the design we discussed.
# Remind that, we are using a Doubly LinkedList with a sentinel head and a cursor pointer.
# The next node of the tail is the sentinel head, and the previous node of the sentinel head is the tail.

class LinkedList:

    # Please implement each of the following methods following the guide.
    # Here, I've only implemented the construction methods and the dunder __repr__ method. Do not change them.
    # Do not use other designs of a LinkedList.

    class Node:
        ####################    DO NOT CHANGE   ####################
        def __init__(self, val, prev = None, next = None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        ####################    DO NOT CHANGE   ####################
        self.head = LinkedList.Node(None) # Sentinel Head, do not delete this node.
        self.head.prev = self.head.next = self.head
        self.cursor = self.head
        self.size = 0

    def __len__(self):
        # return the size of the LinkedList
        return self.size

    def prepend(self, item):
        # Insert item as a node right after the sentinel head.
        # Make sure the pointers are pointing to correct nodes.
        linkedlist = LinkedList.Node(item, self.head, self.head.next)
        self.head.next = linkedlist
        linkedlist.next.prev = linkedlist
        # Remember to increase the size of the LinkedList.
        self.size += 1
        # Don't return anything in this method.

    def append(self, item):
        # Insert item as a node to the tail of the LinkedList
        # Make sure the pointers are pointing to correct nodes.
        linkedlist = LinkedList.Node(item, self.head.prev, self.head)
        linkedlist.prev.next = linkedlist
        self.head.prev = linkedlist
        # Remember to increase the size of the LinkedList.
        self.size += 1
        # Don't return anything in this method.

    def __iter__(self):
        # This is implementing for x in list.
        # Use a generator (with keyword "yield" ) to implement the iterator method.
        self.cursor = self.head.next
        while self.cursor is not self.head:
            yield self.cursor.val
            self.cursor = self.cursor.next

    def __repr__(self):
        ####################    DO NOT CHANGE   ####################
        return "[" + ",".join(repr(x) for x in self ) + "]"

    def cursor_set(self, index):
        assert (isinstance(index, int)) and index >= 0 and index < self.size
        # Move the cursor to the given index.
        self.cursor = self.head
        for _ in range(index + 1):
            self.cursor = self.cursor.next
        # Don't return anything in this method.

    def cursor_get(self):
        assert self.cursor is not self.head
        # return the value in the cursor.
        return self.cursor.val

    def cursor_update(self, item):
        assert self.cursor is not self.head
        # Update the value in the cursor to item.
        self.cursor.val = item
        # Don't return anything in this method.

    def __getitem__(self, index):
        assert (isinstance(index, int))
        # This is implementing list[index].
        # Use cursor_set(.) and cursor_get(.) to return the value in the node at index.
        self.cursor_set(index)
        return self.cursor_get()

    def __setitem__(self, index, item):
        assert (isinstance(index, int))
        # This is implementing list[index] = item.
        # Use cursor_set(.) and cursor_update(.) to update the value in the node at index to item.
        self.cursor_set(index)
        self.cursor_update(item)
        # Don't return anything in this method.

    def cursor_insert(self, item):
        # Insert item as a node after the cursor.
        n = LinkedList.Node(item, self.cursor, self.cursor.next)
        self.cursor.next = n
        # Move the cursor to the inserted node.
        n.next.prev = n
        # Remember to increase the size of the LinkedList.
        self.size += 1
        self.cursor = n
        # Don't return anything in this method.

    def cursor_delete(self):
        assert self.cursor is not self.head and len(self) > 0
        # Delete the cursor node and let cursor.next to be the new cursor.
        self.cursor.prev.next = self.cursor.next
        self.cursor.next.prev = self.cursor.prev
        # Remember to decrease the size of the LinkedList.
        self.size -= 1
        self.cursor = self.cursor.next
        # Don't return anything in this method.

    def __contains__(self, item):
        # This is implementing item in list as a Boolean.

        self.cursor = self.head.next
        while self.cursor is not self.head:
            if self.cursor.val is item:
                return True
            self.cursor = self.cursor.next
            # Return True if item is in the LinkedList, or else return False.
        return False

    def __add__(self, other):
        assert(isinstance(other, LinkedList))
        # This is implementing self + other
        # Append the other list to the tail of the self list.
        # Make sure that all the pointers are pointing to the correct nodes.
        # Remember to change the self.size of the updated list accordingly.
        if len(other) != 0:
            self.head.prev.next = other.head.next
            other.head.next.prev = self.head.prev
            other.head.prev.next = self.head
            self.head.prev = other.head.prev
            self.size += other.size
        # Don't return anything in this method.

    def remove_items(self, item):
        # Remove each node in the list containing item as its value.
        self.cursor = self.head.next
        # If at least one node is removed, remember to decrease the size of the LinkedList.
        while self.cursor is not self.head:
            if self.cursor.val is item:
                self.cursor_delete()
            else:
                self.cursor = self.cursor.next
        # Don't return anything in this method.

    def reverse_list(self):
        # Reverse the order of nodes in the list.
        # For example: if you have a list = SH <-> 1 <-> 3 <-> 5,
        # after reverse_list(), you need to update it to  SH <-> 5 <-> 3 <-> 1.
        # Here, SH means the sentinel head.
        # Since you are updating this list, don't return anything in this method.
        self.cursor = self.head.next
        while self.cursor is not self.head:
            temp = self.cursor.next
            self.cursor.next = self.cursor.prev
            self.cursor.prev = temp
            self.cursor = temp
        self.cursor = self.head.next
        self.head.next = self.head.prev
        self.head.prev = self.cursor


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################
list1 = LinkedList()
for x in range(1,5):
    list1.append(x)
print("Let's start with a list consists of the first four positive integers: list1 =", list1,
      ", and its size =", list1.size, "." )

for x in range(4,8):
    list1.prepend(x)
print("Then we add integers 7,6,5,4 to the front, and list1 =", list1, ", and its size =", list1.size, ".")

list1.remove_items(4)
print("After removing all 4's from list1, we get list1 =", list1, ", and its size =", list1.size, ".")

list1[3] = 8
print("Let's update number 1 in list1 to 8, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.val, ".")

list1.cursor_set(2)
for x in range(9,11):
    list1.cursor_insert(x)
print("Insert number 9 and 10 after number 5, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.val, ".")

list1.cursor_set(1)
for x in range(3):
    list1.cursor_delete()
print("Delete three continuous numbers after 7, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.val, ".")

print("Does list1 contains number 5? The answer is", 5 in list1, ".")

list2 = LinkedList()
list2.cursor_insert(1)
print("Let list2 be a list containing only number 1: list2 =", list2, ".")

list2 + list1
print("If we append list1 to the tail of list2, the new list2 =", list2, ", and its size =", list2.size, ".")

list2.reverse_list()
print("Let's reverse the order of numbers in list2, we get list2 =", list2, ".")

