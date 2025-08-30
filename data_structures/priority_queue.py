# assuming the smallent the number ==> the higher its priority
# if same priority then the one which came first will be gone first

# using list
class priority_queue:
    def __init__(self):
        self.lst = []

    def is_empty(self):
        if self.lst == []:
            return True

        return False
    
    def pop(self):
        if self.is_empty():
            print("Empty")
        return self.lst.pop()
    
    def push(self, data, priority):
        item = (data, priority)
        
        if self.is_empty():
            self.lst.append(item)

        else:
            counter = 0

            for i in self.lst:
                if i[1] <= priority:
                    break          

                counter += 1 

            self.lst.insert(counter, item)


    def size(self):
        return len(self.lst)
    

# using sll
class Node:
    def __init__(self, item, priority, next = None):
        self.item = item
        self.priority = priority
        self.next = next

class priority_queue_sll:
    def __init__(self):
        self.start = None
        self.counter = 0

    def is_empty(self):
        if self.start == None:
            return True

        return False
    
    def pop(self):
        if self.is_empty():
            print("Empty")

        x = self.start
        self.start = self.start.next

        self.counter -= 1

        return (x.item, x.priority)
    
    def push(self, data, priority):
        item = Node(data, priority)
        
        if not self.start or priority < self.start.priority:
            item.next = self.start
            self.start = item
                
        else:
            temp = self.start
            
            while temp != None and temp.priority <= priority:
                t = temp
                temp = temp.next

            '''
            OR

            while temp.next and temp.next.priority <= priority:
                temp = temp.next

            item.next = temp.next
            temp.next = item
            
            
            '''

            item.next = t.next
            t.next = item
                
        self.counter += 1
            

    def size(self):
        return self.counter

    

# using heap

# !!! after learning heap !!!





# testing

pq = priority_queue_sll()

print(pq.is_empty())

pq.push("Hello Guys !!!", 5)
pq.push("Hi, ", 0)
pq.push("I just", 1)
pq.push("say, ", 4)
pq.push("wanted", 2)
pq.push("to", 3)
pq.push("Who are you?", 5)

# print(pq.lst)

temp = pq.start

while temp != None:
    print(temp.item, temp.priority)
    temp = temp.next


print(pq.pop())

print(pq.size())