# creating sll
class sll:
    def __init__(self, start = None):
        self.next = start
        self.start = start

    # checking emptyness
    def is_empty(self):
        if self.next == None :
            return True
        else:
            return False

    # returning what to be iterated
    def __iter__(self):
        return self
    
    # returning for each iteration
    def __next__(self):
        self.temp = self.next

        if self.next != None:
            x = self.next
            self.next = self.next.next

            return x
        
        else:
            self.next = self.start
            raise StopIteration
        
    # to insert a node after one
    # to insert a node at start after = None
    def insert(self, node_obj, after = None):
        if after == None:
            node_obj.next = self.next
            self.next = node_obj
            self.start = node_obj

        else:
            node_obj.next = after.next
            after.next = node_obj

    # to delete a node after a node
    # to delete start node, after = None
    def delete(self, node_obj, after = None):
        before = node_obj.next

        if after == None:
            self.next = before
            self.start = before
        
        else:
            after.next = before


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




# creating a node
class node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next


#Testing

node5 = node(10)
node4 = node(20, node5)
node3 = node(30, node4)
node2 = node(40, node3)
node1 = node(50, node2)

starting = sll(node1)

print(starting.is_empty())

for i in starting:
    print(i.item)

node0 = node(45)
starting.insert(node0, node1)

print()

for i in starting:
    print(i.item)

print()

starting.delete(node0, node1)

for i in starting:
    print(i.item)

print(starting)

print(starting.search(20))
















