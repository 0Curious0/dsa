class deque:
    def __init__(self):
        self.lst = []

    def insert_rear(self, item):
        self.lst.append(item)

    def insert_front(self, item):
        self.lst.insert(0, item)

    def delete_rear(self):
        return self.lst.pop()
    
    def delete_front(self):
        return self.lst.pop(0)
    
    def is_empty(self):
        if self.lst == []:
            return True
        
        return False
    
    def get_front(self):
        return self.lst[0]
    
    def get_rear(self):
        return self.lst[-1]
    
    def size(self):
        return len(self.lst)
    


# deque using dll

#creating a node
class node: 
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class deque_dll:
    def __init__(self):
        self.front = None
        self.rear = None
        self.counter = 0

    def insert_rear(self, item):
        if self.front == None:
            n = node(item)

            self.front = n
            self.rear = n

            self.counter += 1

        elif self.front.next == None:
            n = node(item)
            
            n.prev = self.front
            self.front.next = n
            self.rear = n

            self.counter += 1

        else:
            n = node(item)
            
            n.prev = self.rear
            self.rear.next = n
            self.rear = self.rear.next

            self.counter += 1


    def insert_front(self, item):
        if self.front == None:
            n = node(item)

            self.front = n
            self.rear = n

            self.counter += 1

        else:
            n = node(item)

            n.next = self.front
            self.front.prev = n

            self.front = n

            self.counter += 1


    def delete_rear(self):
        if self.front == None:
            print("Deque is Empty")

        elif self.front.next == None:
            self.front = None
            self.rear = None

            self.counter -= 1

        else:
            self.rear.prev.next = None
            self.rear = self.rear.prev

            self.counter -= 1
    
    def delete_front(self):
        if self.front == None:
            print("Deque is Empty")

        elif self.front.next == None:
            self.front = None
            self.rear = None

            self.counter -= 1

        else:
            self.front.next.prev = None
            self.front = self.front.next

            self.counter -= 1
    
    def is_empty(self):
        if self.front == None:
            return True
        
        return False
    
    def get_front(self):
        return self.front.item
    
    def get_rear(self):
        return self.rear.item
    
    def size(self):
        return self.counter



# Testing

q = deque_dll()

q.insert_front(10)
q.insert_front(20)
q.insert_rear(30)
q.insert_rear(40)
q.insert_rear(50)

temp = q.front
while temp != None:
    print(temp.item)
    temp = temp.next

# print(q.lst)

q.delete_front()
q.delete_rear()

temp = q.front
while temp != None:
    print(temp.item)
    temp = temp.next
    
print(q.is_empty())
print(q.size())
print(q.get_front())
print(q.get_rear())

# print(q.lst)