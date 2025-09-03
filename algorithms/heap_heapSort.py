class heap:
    def __init__(self):
        self.lst = []

    def createHeap(self, lst):
        for i in lst:
            self.insert(i)

    def insert(self, value):
        index = len(self.lst)
        parent = (index - 1)//2

        self.lst.append(value)

        while self.lst[index] > self.lst[parent] and parent >= 0:
            self.lst[parent], self.lst[index] = self.lst[index], self.lst[parent]

            index = parent
            parent = (parent-1)//2
        

        '''
        index = len(self.lst)
        parent = (index - 1)//2

        while index > 0 and self.lst[parent] < value:
            if index == len(self.lst):
                self.lst.append(self.lst[parent])

            else:
                self.lst[index], self.lst[parent] = self.lst[parent], self.lst[index]

        if index = len(self.lst):
            self.lst.append(value)

        else:
            self.lst[index] = value
        
        '''


    def delete(self):
        if len(self.lst) == 0:
            raise EmptyHeapException()
        
        if len(self.lst) == 1:
            return self.lst.pop()
        
        temp = self.lst.pop()
        top = self.lst[0]
        self.lst[0] = temp

        index = 0
        left = 1
        right = 2

        while left < len(self.lst) and right < len(self.lst) and self.lst[index] < max(self.lst[right], self.lst[left]):
            if self.lst[right] >= self.lst[left]:
                self.lst[right], self.lst[index] = self.lst[index], self.lst[right]
                index = right

            else:
                self.lst[left], self.lst[index] = self.lst[index], self.lst[left]
                index = left
            
            left = 2*index + 1
            right = 2*index + 2


        if left < len(self.lst) and right >= len(self.lst):
            if self.lst[left] > self.lst[index]:
                self.lst[left], self.lst[index] = self.lst[index], self.lst[left]
        
        return top
    

        '''
        while left<len(self.lst):
            if right<len(self.lst):
                if self.lst[left] > self.lst[right]:
                    if self.lst[left] > temp:
                        self.lst[index] = self.lst[left]
                        index = left

                    else:
                        break
                
                else:
                    if self.lst[right] > temp:
                        self.lst[index] = self.lst[right]
                        index = right

                    else:
                        break
            
            else: #No right child
                if self.lst[left] > temp:
                    self.lst[index] = self.lst[left]
                    index = left
                else:
                    break
                    
        self.lst[index] = temp

        return top                    
        
        '''
    
        
    def top(self):
        if len(self.lst) == 0:
            raise EmptyHeapException()
        
        return self.lst[0]

    def heapSort(self, list1):
        self.createHeap(list1)
        list2 = []

        try:
            while True:
                list2.insert(0, self.delete())

        except EmptyHeapException:
            pass

        return list2




class EmptyHeapException(Exception):
    def __init__(self, msg = "Empty Heap"):
        self.msg = msg

    def __str__(self):
        return self.msg


# Testing

h = heap()

lst = [40, 70, 10, 90, 60, 30, 50, 20, 80]

h.createHeap(lst)
print(h.lst)

h = heap()
lst1 = h.heapSort(lst)
print(lst1)


