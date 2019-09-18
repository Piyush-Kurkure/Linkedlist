class Node:
    def __init__(self,data):
        self.data = data    #assisgn data
        self.next = None    #assign next as NULL

class LinkedList:
    def __init__(self):     #initialize LL object
        self.head = None    #assign initial node as NULL

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linkedlist = LinkedList()    #object as empty list

    linkedlist.head = Node(1)   #create 3 nodes
    Second = Node(2)
    Third = Node(3)

    #linking the nodes
    linkedlist.head.next = Second
    Second.next = Third

    linkedlist.printlist()

