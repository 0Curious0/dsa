class queue:
    def __init__(self):
        self.lst = []

    def enqueue(self, item):
        self.lst.append(item)

    def dequeue(self):
        return self.lst.pop(0)

    def is_empty(self):
        if self.lst == []:
            return True
        
        return False

    def size(self):
        return len(self.lst)

    def get_front(self):
        return self.lst[0]

    def get_rear(self):
        return self.lst[-1]
    

class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class queue_using_sll:
    def __init__(self, start = None):
        self.front = start
        self.rear = start
        self.counter = 0

    def enqueue(self, item):
        n = Node(item)

        if self.is_empty():
            self.front = n
            self.rear = n
            self.counter += 1

            return
        
        elif self.front.next == None:
            self.front.next = n
            self.rear = n

            self.counter += 1

        else:
            self.rear.next = n
            self.rear = n

            self.counter += 1

        

    def dequeue(self):
        if self.is_empty():
            print("Empty Queue")
        
        elif self.front.next == None:
            self.front = None
            self.rear = None

            self.counter -= 1

        else:
            self.front = self.front.next
            self.counter -= 1

    def is_empty(self):
        if self.front == None:
            return True
        
        return False

    def size(self):
        return self.counter

    def get_front(self):
        return self.front.item

    def get_rear(self):
        return self.rear.item

    
    



# Testing

q = queue_using_sll()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

temp = q.front
while temp != None:
    print(temp.item)
    temp = temp.next

# print(q.lst)

q.dequeue()
q.dequeue()

temp = q.front
while temp != None:
    print(temp.item)
    temp = temp.next
    
print(q.is_empty())
print(q.size())
print(q.get_front())
print(q.get_rear())

# print(q.lst)


