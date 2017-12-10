class node:
    def __init__(self, data=None, prev=None, next=None): 
        self.data = data
        self.prev = prev
        self.next = next
    def setNext(self,next):
        self.next = next
    def setPrev(self,prev):
        self.prev=prev
    def setData(self,data):
        self.data = data

class SinglylinkedList:
    def __init__(self,head, distinct=False):
        self.head = head
        self.end = head
        self.distinct = distinct
    def GetIndexNode(self,index):
        if self.head == None:
            return 0
        currentNode = self.head
        position = 0
        while position < index:
            if currentNode.next == None:
                raise Exception('the index is outside of the linkedList bounds')
            currentNode = currentNode.next
            position += 1
        return currentNode
    def GetIndexData(self,index):
        if self.head == None:
            return 0
        currentNode = self.head
        position = 0
        while position < index:
            if currentNode.next == None:
                raise Exception('the index is outside of the linkedList bounds')
            currentNode = currentNode.next
            position += 1
        return currentNode.data        
    def Head(self):
        return self.head
        
    def Tail(self):
        if self.head == None:
            return None
        return self.head.next

    def Count(self):
        if self.head == None:
            return 0
        length = 1
        currentNode = self.head
        while currentNode.next != None:
            length +=1
            currentNode = currentNode.next
        return length

    def InsertAfterIndex(self, node, index):
        currentNode = self.GetIndexNode(index)
        node.setNext(currentNode.next)
        currentNode.setNext(node)
    def Contains(self, value):
        currentNode = self.head
        while currentNode != None:
            if currentNode.data == value:
                return True
            currentNode = currentNode.next
        return False
    def Add(self, newNode):
        if not self.distinct:
            self.end.setNext(newNode)
            self.end = newNode
        else:
            currentNode = self.head
            while currentNode.next != None:
                if currentNode.data == newNode.data:
                    return
                currentNode = currentNode.next
            currentNode.setNext = newNode
    def RemoveHead(self):
        self.head = self.head.next;
    def RemoveIndex(self,index):
        if index is 0:
            self.RemoveHead()
            return
        currentNode = self.head
        position = 1
        while position < index:
            if currentNode.next == None:
                raise Exception('the index is outside of the linkedList bounds')
            currentNode = currentNode.next
            position += 1        
        currentNode.setNext(None if currentNode.next is None else currentNode.next.next)
    def RemoveFirstValue(self, value):
        currentNode = self.head
        while currentNode.next != None and currentNode.next.value != value:
            currentNode = currentNode.next
        if currentNode.next == None:
            return
        currentNode.setNext(currentNode.next.next)
    def PrintList(self, head = None):
        currentNode = head if head is not None else self.head
        while currentNode.next is not None:
            print(currentNode.data, end=", ")
            currentNode = currentNode.next
        print(currentNode.data)
class DoublylinkedList(SinglylinkedList):
    def __init__(self,head=None, distinct=False):
        self.head = head
    def getIndex(self,index):
        pass
    def getFirst(self,value):
        pass
    def head(self):
        pass
    def tail(self):
        pass
    def count(self):
        pass
    def insertAtIndex(self):
        pass
    def add(self):
        pass
    def removeFirst(self):
        pass
    def removeIndex(self):
        pass
    def removeValue(self):
        pass
