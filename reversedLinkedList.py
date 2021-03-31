# a -> b -> c -> d -> None
# d -> c -> b -> a -> None
'''def reversedLinkedList(head):
    curr = head
    previous = None
    while True:
        if not curr.next:
            break
        tmp_curr = curr.next
        curr.next = previous
        previous = curr
        curr = tmp_curr
    return curr'''

'''class LinkedList:
    def __init__(self, value):
        self.value = value
            self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

llist = LinkedList()
llist
>>> first_node = Node("a")
>>> llist.head = first_node
>>> llist
a -> None

>>> second_node = Node("b")
>>> third_node = Node("c")
>>> first_node.next = second_node
>>> second_node.next = third_node
>>> llist