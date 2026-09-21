class DynamicArray:

    def __init__(self, capacity: int):
        if capacity <=0:
            self.array = []
        arr = [0 for _ in range(capacity)]
        self.array = arr
        self.capacity = capacity
        self.items = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.getCapacity() == self.items:
            self.resize()
        self.array[self.items] = n
        self.items += 1


    def popback(self) -> int:

        self.items -= 1
        tmp = self.array[self.items]
        self.array[self.items] = 0
        return tmp
 

    def resize(self) -> None:
        length = self.capacity * 2
        newArr = [0 for i in range(length)]
        for i in range(len(self.array)):
            newArr[i] = self.array[i]
        self.array = newArr
        self.capacity = self.capacity * 2



    def getSize(self) -> int:
        return self.items
        
    
    def getCapacity(self) -> int:
        return self.capacity
        

