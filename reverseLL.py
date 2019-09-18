class Node:
    def __init__(self, data):
        self.data = data  # assisgn data
        self.next = None  # assign next as NULL


class LinkedList:
    def __init__(self):  # initialize LL object
        self.head = None  # assign initial node as NULL

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, newdata):
        newnode = Node(newdata)  # 1.Allocate node and 2.put data in it
        newnode.next = self.head  # 3.Make next of new node as head
        self.head = newnode  # 4.Move head to new node

    def reverse(self):
        curr = self.head        #initialize the pointer
        prev = None
        while curr is not None:
            forward = curr.next     # We need something in front to traverse
            curr.next = prev        # Change the direction of flow
            prev = curr             # Increment prev
            curr = forward          # Increment curr
        self.head = prev

if __name__ == '__main__':
    linkedlist = LinkedList()  # object as empty list

    linkedlist.push(1)
    linkedlist.push(2)
    linkedlist.push(3)
    linkedlist.push(4)
    linkedlist.reverse()
    linkedlist.printlist()

