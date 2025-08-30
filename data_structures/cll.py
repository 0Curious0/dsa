class cll:
    def __init__(self, last):
        self.last = last
    
    def is_empty(self):
        if self.last == None:
            return True
        
        return False
    
    def insert_at_start(self, node):
        if self.is_empty():
            self.last = node

        else:
            node.next = self.last.next
            self.last.next = node

    def insert_at_end(self, node):
        if self.is_empty():
            self.last = node
            self.temp = self.last.next

        else:
            node.next = self.last.next
            self.last.next = node
            self.last = node

    def insert_after(self, node, after):
        node.next = after.next
        after.next = node

    def __iter__(self):
        temp = self.last.next

        while temp != self.last:
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
        self.last.next = self.last.next.next

    def delete_at_end(self):
        for i in self:
            if i.next == self.last:
                i.next = self.last.next
                self.last = i
        


    def delete_after(self, after):
        after.next = after.next.next
    



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

node5.next = node1

circular = cll(node5)


for i in circular:
    print(i.item)

print()

print(circular.search(40))

print()

node0 = node(0, None)
node01 = node(1, None)
node02 = node(2, None)

circular.insert_at_start(node0)

circular.insert_at_end(node01)
circular.insert_after(node02, node1)

for i in circular:
    print(i.item)

print()

circular.delete_at_start()

# circular.delete_at_end()
circular.delete_after(node1)

for i in circular:
    print(i.item)


