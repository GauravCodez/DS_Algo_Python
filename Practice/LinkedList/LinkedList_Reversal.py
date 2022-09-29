# Write a program to reverse the linked list

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

    def reverse(self):
        # Interchanging the Head and Tails with the help of using a temp variable
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(9)
my_linked_list.append(11)
my_linked_list.append(13)
my_linked_list.append(15)
my_linked_list.print_list()

print("------------------")
print("Reversing the LinkedList")
my_linked_list.reverse()
my_linked_list.print_list()
print("Thanks !!")
