class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add node to the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Add node to the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    # Insert after a given node
    def insert_after(self, prev_node, data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    # Insert before a given node
    def insert_before(self, next_node, data):
        if not next_node:
            return
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    # Remove a node by value
    def remove(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                current_node.prev = None
                current_node.next = None
                return True
            current_node = current_node.next
        return False

    # Search for a node by value
    def search(self, target_data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                return current_node
            current_node = current_node.next
        return None
    
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()



dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.push(0)
node_2 = dll.search(2)
if node_2:
    dll.insert_after(node_2, 2.5)
node_2_5 = dll.search(2.5)
if node_2_5:
    dll.insert_before(node_2_5, 2.25)
dll.remove(2.5)

print("List from head to tail:")
dll.print_forward()

print("List from tail to head:")
dll.print_backward()
