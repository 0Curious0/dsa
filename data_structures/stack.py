# stack creation using list 
class stack_with_list:
    def __init__(self):
        self.lst = []

    def is_empty(self):
        if self.lst == []:
            return True

        return False

    
    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if self.lst != []:
            return self.lst.pop()

        else:
            print("Stack is empty")

    def peek(self):
        return self.lst[-1]
    
    def size(self):
        return len(self.lst)
    
    def show(self):
        print(self.lst)
    



# stack creation by inheriting list class
class stack_inheriting_list(list):
    def __init__(self):
        self.push = self.append
        self.size = self.__len__

    def is_empty(self):
        if self == []:
            return True

        return False
    
    def pop(self):
        if self != []:
            return super().pop()

        else:
            print("Stack is empty")
        

    def peek(self):
        return self[-1]
    
    def insert(self, index, data):
        raise AttributeError("No Attribute 'insert' in Stack")
    



# stack creation by creating a SLL inside with top variable to track a record of the new entry
 
class node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class stack_combined_with_sll:
    def __init__(self, top = None):
        self.top = top

    def is_empty(self):
        return self.top == None
        
    def push(self, data):
        if self.is_empty() :
            self.top = node(data)

        else:
            n = node(data)
            n.next = self.top
            self.top = n

    def pop(self):
        if self.is_empty():
            print("Empty Stack can't pop")
            return
        
        x = self.top.item
        self.top = self.top.next
        return x
    
    def peek(self):
        return self.top.item
    
    def size(self):
        counter = 0

        temp = self.top
        while temp != None:
            counter += 1
            temp = temp.next

        return counter
    
    def show(self):
        lst = []

        temp = self.top
        while temp != None:
            lst.append(temp.item)
            temp = temp.next

        return lst
        
  


# stack creation using sll
class sll:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        if self.start == None :
            return True
        else:
            return False


    def __iter__(self):
        self.temp = self.start

        return self
    
    def __next__(self):
        if self.temp != None:
            x = self.temp
            self.temp = self.temp.next

            return x
        
        else:
            raise StopIteration
        
    def insert(self, node_obj, after = None):
        if after == None:
            node_obj.next = self.next
            self.next = node_obj
            self.start = node_obj

        else:
            node_obj.next = after.next
            after.next = node_obj

    def insert_at_start(self, node):
        if self.is_empty():
            self.start = node

        else:
            node.next = self.start
            self.start = node

    def insert_at_end(self, node):
        temp = self.start

        while temp.next != None:
            temp = temp.next

        temp.next = node
            

    def delete_obj(self, node_obj, after = None):
        before = node_obj.next

        if after == None:
            self.next = before
            self.start = before
        
        else:
            after.next = before


    def delete_at_start(self):
        self.start = self.start.next

    def delete_at_end(self):
        temp = self.start

        while temp.next.next != None:
            temp = temp.next

        temp.next = None
    


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



class stack_with_sll:
    def __init__(self):
        self.lst = sll(None)
        self.counter = 0

    def is_empty(self):
        if self.lst == []:
            return True

        return False

    
    def push(self, item):
        self.lst.insert_at_start(node(item))
        self.counter += 1

    def pop(self):
        x = self.lst.start
        self.lst.delete_at_start()

        self.counter -= 1

        return x.item

    def peek(self):
        return self.lst.start.item
    
    def size(self):
        return self.counter

    
    def show(self):
        print(self.lst)

    
# stack created by inheriting sll

class stack_inheriting_sll(sll):
    def __init__(self):
        super().__init__()
        self.counter = 0
        
    def push(self, item):
        self.insert_at_start(node(item))
        self.counter += 1

    def pop(self):
        if not self.is_empty():
            x = self.start

            self.delete_at_start()
            self.counter -= 1

            return x.item

            

        else:
            print("Stack is empty")

    def peek(self):
        return self.start.item
    
    def size(self):
        return self.counter

    
    def show(self):
        temp = self.start
        lst = []

        while temp != None:
            lst.append(temp.item)
            temp = temp.next

        print(lst)
            

    def __iter__(self):
        raise AttributeError("No Iter Attribute")
    
    def search(self):
        raise AttributeError("No Search Attribute")
    
    def insert(self):
        raise AttributeError("No Insert Attribute")
    
    def insert_at_end(self):
        raise AttributeError("No Insert at End Attribute")
    
    def delete_obj(self):
        raise AttributeError("No Delete Obj Attribute")
    
    def delete_at_end(self):
        raise AttributeError("No Delete at End Attribute")
    
    






# Testing

stk = stack_inheriting_sll()


stk.push(1)
stk.push(2)
stk.push(4)

print(stk.pop())
print(stk.peek())
print(stk.size())
print(stk.is_empty())
stk.show()


