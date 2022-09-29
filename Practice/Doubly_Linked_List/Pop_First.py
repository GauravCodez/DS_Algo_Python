# Perform the pop first operation on doubly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DDL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def pre_pend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            # Commented as prev link is already established in the constructor
            # Hence no need to again assign prev value
            # new_node.prev = None
            self.head = new_node
        self.length += 1
        return new_node.value

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp


my_linked_list = DDL(3)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(9)
my_linked_list.append(11)
print(my_linked_list.print_list())
print("Popping the value at the last end of the doubly linked list : ")
print(my_linked_list.pop())
print("After performing the pop operation, the linked list is listed below : ")
print(my_linked_list.print_list())
my_linked_list.pre_pend(21)
print("Doubly linked list after performing the pre-pend operation : ")
print(my_linked_list.print_list())

my_linked_list.pop_first()
print("Doubly linked list after performing the pop first operation : ")
print(my_linked_list.print_list())
