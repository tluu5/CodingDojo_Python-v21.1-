from http.client import NETWORK_AUTHENTICATION_REQUIRED
from multiprocessing.sharedctypes import Value


class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = new_node 
        return self
    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        return self
    def remove_from_back(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
        return self
class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
sll = SList()
#sll.add_to_front("B").add_to_front("A").add_to_back("C").remove_from_front().print_values()
sll2 = SList()
sll2.add_to_back("Z").add_to_back("Y").remove_from_back().remove_from_back().print_values()