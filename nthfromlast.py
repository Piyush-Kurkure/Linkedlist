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

    def nthfromlast(self,n):
        temp = self.head
        # Calculate length
        length = 0
        while(temp is not None):
            length = length + 1
            temp = temp.next
        if n>length:
            print("Value is greater")
            return
        temp = self.head
        for i in range(length-n):
            temp= temp.next
        print(temp.data)

    def middle(self):
        temp = self.head
        # Calculate length
        length = 0
        while (temp is not None):
            length = length + 1
            temp = temp.next
        temp = self.head
        for i in range(length//2):
            temp = temp.next
        print(temp.data)
if __name__ == '__main__':
    linkedlist = LinkedList()  # object as empty list

    linkedlist.push(1)
    linkedlist.push(2)
    linkedlist.push(3)
    linkedlist.push(4)
    linkedlist.push(5)
    linkedlist.middle()
    linkedlist.nthfromlast(4)
    linkedlist.printlist()

