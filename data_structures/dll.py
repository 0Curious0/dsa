class dll:
    def __init__(self, start = None):
        self.start = start
        self.temp = self.start

    # returning what to be iterated
    def __iter__(self):
        return self
    
    # returning for each iteration
    def __next__(self):
        if self.temp != None:
            x = self.temp
            self.temp = self.temp.next

            return x
        
        else:
            self.temp = self.start
            raise StopIteration
        

    # inserting a node in between two 
    # at start prev = none
    # at end next = none
    def insert(self, node, prev = None, next = None):
        if prev == None :
            node.next = self.start
            self.start = node
            self.temp = self.start

        else:
            node.next = prev.next
            prev.next = node

    
    # deleting a node in between two 
    # at start prev = none
    # at end next = none
    def delete(self, prev = None, next = None):
        if prev == None :
            self.start = next
            self.temp = self.start

        else:
            prev.next = next


    # checking emptyness
    def is_empty(self):
        if self.next == None :
            return True
        else:
            return False
        
    def __str__(self):
        lst = [i.item for i in self]
        return str(lst)
    

    def search(self, value):
        counter = 1
        lst = []

        for i in self:
            if i.item == value:
                lst.append((i, f"is the node with this value at position {counter}"))
            
            counter +=1
        
        if lst == []:
            return "Not Found"

        return lst




#creating a node
class node: 
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next


#Testing

node1 = node(50)

node2 = node(40, node1)
node1.next = node2

node3 = node(30, node2)
node2.next = node3

node4 = node(20, node3)
node3.next = node4

node5 = node(10, node4)
node4.next = node5

node0 = node(0)




double = dll(node1)

for i in double:
    print(i.item)

print()


double.insert(node0, node1, node2)

for i in double:
    print(i.item)

print()


double.delete(node1, node2)

for i in double:
    print(i.item)

print(double)


print(double.search(0))


