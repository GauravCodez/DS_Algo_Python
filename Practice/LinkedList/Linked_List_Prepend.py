# Program to prepend a new node to the Linked List

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

print("The new Linked List is as follows : ")
print(my_linked_list.print_list())
