class Node:
    def __init__(self, value, nextN=None):
        
        self.value = value
        self.nextN = nextN

class LinkedList:
    
    def __init__(self):
        self.llist = Node(-1)
        self.tail = self.llist

    def findTmp(self, index: int) -> Node:
        tmp = self.llist.nextN #avoid the dummy node
        ind = 0
        while tmp:
            if ind == index:
                return tmp
           
            ind +=1
            tmp = tmp.nextN
        return None
    
    def get(self, index: int) -> int:
        tmp = self.findTmp(index)
        return tmp.value if tmp != None else -1
        

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        #get the next of the dummy head to put that next
        newHead.nextN = self.llist.nextN
        #move the dummy head to point at the new head
        self.llist.nextN = newHead
        #if the list is empty then also reset the tail
        if not newHead.nextN:
            self.tail = newHead

        

    def insertTail(self, val: int) -> None:
        self.tail.nextN = Node(val)
        self.tail = self.tail.nextN

       
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.llist
        while i < index and curr:
            i += 1
            curr = curr.nextN

        if curr and curr.nextN:
            if curr.nextN == self.tail:
                self.tail = curr
            curr.nextN = curr.nextN.nextN
            return True
        return False
        

    def getValues(self) -> List[int]:
        vals = []
        tmp = self.llist.nextN
        while tmp:
            print(f" {tmp.value} and {tmp.nextN}")
            vals.append( tmp.value)
            tmp = tmp.nextN
        return vals
        

