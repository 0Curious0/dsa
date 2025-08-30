class cdll:
    def __init__(self, start):
        self.start = start

    def is_empty(self):
        if self.start == None:
            return True

        return False
    
    def insert_at_start(self, node):
        if self.is_empty():
            self.start = node

        else:
            node.next = self.start
            node.prev = self.start.prev
            self.start = node


    def insert_at_last(self, node):
        node.next = self.start
        node.prev = self.start.prev
        self.start.prev.next = node
        self.start.prev = node

    def insert_after(self, after, node):
        if after != None:
            node.next = after.next
            after.next = node
            node.prev = after

        else:
            self.insert_at_start(node)


    def __iter__(self):
        temp = self.start

        while temp != self.start.prev:
            yield temp
            temp = temp.next

        yield temp


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
    
    def delete_at_start(self):
        self.start.next.prev = self.start.prev
        self.start = self.start.next

        if self.start.next == None:
            self.start = None

    def delete_at_last(self):
        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev
    
    def delete_item(self, item):
        lst = self.search(item)

        for i in lst:
            if i[0] == self.start:
                self.delete_at_start()
            else:  
                i[0].prev.next = i[0].next
                i[0].next.prev = i[0].prev


# creating a node
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

node1.prev = node5
node5.next = node1



dcirc = cdll(node1)


for i in dcirc:
    print(i.item)

print()



node0 = node(2)
node01 = node(1)
node02 = node(2)

dcirc.insert_at_start(node0)

dcirc.insert_at_last(node01)
dcirc.insert_after(node1, node02)

for i in dcirc:
    print(i.item)



print()

print(dcirc)

print()



print(dcirc.search(2))
print()



# dcirc.delete_at_start()

dcirc.delete_at_last()
dcirc.delete_item(2)

for i in dcirc:
    print(i.item)










        