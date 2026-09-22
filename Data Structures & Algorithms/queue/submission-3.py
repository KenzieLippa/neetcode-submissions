class Deque:
    
    def __init__(self):
        self.queue = []
        self.length = 0


    def isEmpty(self) -> bool:
        return True if self.length == 0 else False
        

    def append(self, value: int) -> None:
        print(f"but before this is the length: {self.length}")
        self.queue.append(value)
        self.length += 1
        print(f"and now the length is: {self.length}")
        

    def appendleft(self, value: int) -> None:
        newQueue = [value]
        print(newQueue)
        for i in range(self.length):
            newQueue.append(self.queue[i])
        print(f"this is the new queue after: {newQueue}")
        self.queue = newQueue
        self.length +=1
        print(f"and now the length is: {self.length}")
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.length -= 1
        return self.queue.pop()
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.queue[0]
        newQueue = []
        for i in range(1,self.length):
            newQueue.append(self.queue[i])
        self.length = len(newQueue)
        self.queue = newQueue
        return val
        
        
