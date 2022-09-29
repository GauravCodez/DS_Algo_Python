# Remove a node to the linked list  - practice

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 1:
                self.tail = None
        return temp.value

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp = value
        return True

    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove_node(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.pop_first()
            return True
        if index == self.length:
            self.pop()
            return True
        prev = self.get_value(index-1)
        # we are not using nod_to_be_removed = self.get_value(index) since the get_value method is of the O(n)
        # complexity, whereas using prev.next is a good and time saving option than choosing prev.get_value(index)
        nod_to_be_removed = prev.next
        prev.next = nod_to_be_removed.next
        nod_to_be_removed.next = None
        self.length -= 1
        return nod_to_be_removed


my_linked_list = LinkedList(50)
my_linked_list.append(25)
my_linked_list.append(5)
my_linked_list.append(1)
print("The value before applying pop operation : ")
my_linked_list.print_list()
print("Popped values after applying pop operation : ")
print(my_linked_list.pop())
print(my_linked_list.pop())

print("Pre-pending the 2 new values : ")
print("Adding 101 : ", my_linked_list.prepend(101))
print("Adding the 110 : ", my_linked_list.prepend(110))

print("The new Linked List after pre-pend operation is as follows : ")
print(my_linked_list.print_list())

my_linked_list.pop_first()
print("The linked list after applying the pre-pend operation is as follows : ")
print(my_linked_list.print_list())

print("Getting the value of the 3rd element : ")
# Providing the index as 2 for the 3rd element, as the range starts with 0,1,2
print(my_linked_list.get_value(2))

print("Setting the value of the 3rd element as 7 : ")
print(my_linked_list.set_value(2, 7))

print("After setting the value of the 3rd element as 7, the new linked list is listed below : ")
print(my_linked_list.print_list())

my_linked_list.insert_node(1, 1)

print("------------->")
print("The new linked List after performing the linked list insert operation : ")
my_linked_list.print_list()

my_linked_list.remove_node(1)
print("------------->")
print("The new linked List after performing the linked list removal operation : ")
my_linked_list.print_list()
