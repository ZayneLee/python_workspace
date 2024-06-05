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
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
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
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            tmp = self.head
            pre = self.head
            while(tmp.next):
                pre = tmp
                tmp = tmp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        # tmp = self.head
        # self.head = new_node
        # self.head.next = tmp
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
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return tmp

my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()

print('After pop - Linked List:')
my_linked_list.pop()
my_linked_list.print_list()

print('After prepend - Linked List:')
my_linked_list.prepend(0)
my_linked_list.print_list()

print('After pop_first - Linked List:')
my_linked_list.pop_first()
my_linked_list.pop_first()
my_linked_list.print_list()




"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""