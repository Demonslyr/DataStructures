import random
import linkedLists as lList

def buildLinkedList(dataList):
    myList = lList.SinglylinkedList(lList.node(data = dataList[0]))
    for entry in range(1,len(dataList)):
        myList.Add(lList.node(data = dataList[entry]))
    return myList
def main():
    
    testList = buildLinkedList([0,1,2,3,4,5,6,7,8,9])
    print("Testing PrintList()")
    testList.PrintList()
    print("Testing PrintList(node)")
    testList.PrintList(testList.Tail())
    print("Pass!" if testList.Count() == 10 else "Fail!","Testing ListCount")
    print("Pass!" if testList.GetIndexNode(4).data == 4 else "Fail!","Testing GetIndexNode")
    print("Pass!" if testList.GetIndexData(4) == 4 else "Fail!","Testing GetIndexData")
    print("Pass!" if testList.Head().data == 0 else "Fail!","Testing GetHead")
    print("Pass!" if testList.Tail().data == 1 else "Fail!","Testing GetTail")
    testList.InsertAfterIndex(lList.node(data = 1337),5)
    print("Pass!" if testList.GetIndexData(6) == 1337 else "Fail!","Testing InsertAtIndex")
    print("Pass!" if testList.Contains(1337) else "Fail!","Testing Contains")
    testList.RemoveIndex(6)
    print("Pass!" if not testList.Contains(1337) else "Fail!","Testing RemoveIndex")
    testList.RemoveHead()
    print("Pass!" if not testList.Contains(0) else "Fail!","Testing RemoveHead")
    print("Finished!")
if __name__ == "__main__":
    main()