class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newnode = Node(newdata)  # 1.Allocate node and 2.put data in it
        newnode.next = self.head  # 3.Make next of new node as head
        self.head = newnode  # 4.Move head to new node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete(self,value):
        temp = self.head
        if temp is not None:
            if temp.data==value:
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next

        temp = None

    def count(self):
        count = 0
        temp =self.head
        while(temp is not None):
            count = count + 1
            temp = temp.next
        return count

linkedlist = LinkedList()
linkedlist.push(1)
linkedlist.push(2)
linkedlist.push(3)
linkedlist.push(4)

linkedlist.printlist()
print(linkedlist.count())