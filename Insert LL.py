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

    def insertafter(self,prevnode,newdata):
        if prevnode is None:            # 1. If there is no node
            print("No such data found")
            return
        newnode = Node(newdata)     # 2.Allocate new node and 3. put data in it
        newnode.next = prevnode.next    # 4. Make next of new Node as next of prev_node
        prevnode.next = newnode         # 5. Make next of prev_node as new_node

    def append(self, new_data):
        newnode = Node(new_data)         # 1. Allocate new node and 2. put data in it
        if self.head is None:            # 3. If the Linked List is empty
            self.head = newnode
            return
        last = self.head                # 4. Traverse till last node
        while last.next:
            last = last.next
        last.next = newnode            # 5. Change next of last node

if __name__ == '__main__':
    linkedlist = LinkedList()  # object as empty list

    linkedlist.push(1)
    linkedlist.push(2)

    linkedlist.insertafter(linkedlist.head,3)

    linkedlist.append(4)

    linkedlist.printlist()

