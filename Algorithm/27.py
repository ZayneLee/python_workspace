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
            while tmp.next:
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

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head

        for _ in range(index):
            tmp = tmp.next

        return tmp

    def set_value(self, index, value):
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False


my_linked_list = LinkedList(1)

my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.set_value(1, 2)

my_linked_list.print_list()
