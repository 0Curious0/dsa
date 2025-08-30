class Node:
    def __init__(self, item, left=None, right=None):
        self.left = left
        self.right = right
        self.item = item

class BST:
    def __init__(self, root = None):
        self.root = root

    def insert(self, value):
        node = Node(value) 
        temp = self.root

        duplicate = self.search(value)

        if duplicate != None:
            return "Duplication is not allowed"
        
        if self.root == None:
            self.root = node
            return

        while (temp.item < value and temp.right != None) or (temp.item > value and temp.left != None) :
            if temp.item < value:
                temp = temp.right

            else:
                temp = temp.left
            
        if temp.item < value:
            temp.right = node

        else:
            temp.left = node



    """

    # recursion insertion approach

    def insert(self, data):
        self.root = self.rinsert(self.root, data)


    def rinsert(self, temp, data):
        if temp is None:
            return Node(data)
        
        elif data < temp.item:
            temp.left = self.rinsert(temp.left, data)

        elif data > temp.item:
            temp.right = self.rinsert(temp.right, data)

        return temp

    """
        
        
        


    def delete(self, value):
        node = self.search(value)

        if node == None:
            return "No such Node"
        
        else:
            temp = self.root

            while temp.left != node and temp.right != node:
                if temp.item > node.item :
                    temp = temp.left

                else:
                    temp = temp.right



            parent = temp
          
            if node.left == None and node.right == None:
                if parent.left == node:
                    parent.left = None

                else:
                    parent.right = None

            elif node.left == None:
                if parent.left == node:
                    parent.left = node.right

                else:
                    parent.right = node.right

            elif node.right == None:
                if parent.left == node:
                    parent.left = node.left

                else:
                    parent.right = node.left

            else:
                # replacing by successor

                temp = node.right

                while temp.left != None:
                    temp = temp.left

                self.delete(temp.item)

                # if parent.left == node:
                #     parent.left = temp
                #     temp.right = node.right
                #     temp.left = node.left

                # else:
                #     parent.right = temp
                #     temp.right = node.right
                #     temp.left = node.left

                # OR

                node.item = temp.item

    """
    # recursive delete approach

    # is data is not in the tree then temp will become None and no change in tree will occur

    def delete(self, data):
        self.root = self.rdelete(self.root, data)

    def rdelete(self, temp, data):
        if temp == None:
            return temp
        
        elif temp.item > data:
            temp.left = self.rdelete(temp.left, data)
        
        elif temp.item < data:
            temp.right = self.rdelete(temp.right, data)

        else:
            if temp.right is None:
                return temp.left
            
            elif temp.left is None:
                return temp.right
            
            else:
                # replacing by successor

                successor = temp.right

                while successor.left != None:
                    successor = successor.left

                self.delete(successor)

                temp.item = successor.item

        return temp

    """
        


    def search(self, value):
        temp = self.root

        while temp != None:
            if temp.item < value:
                temp = temp.right

            elif temp.item > value:
                temp = temp.left
            
            else:
                return temp

        return None
    
    """
    # recursive search approach
    def search(self, value):
        return self.rsearch(self.root, value)
    
    def rsearch(self, temp, value):
        if temp is None or temp.item == value:
            return temp
        
        elif temp.item > value:
            return self.rsearch(temp.left, value)
        
        else:
            return self.rsearch(temp.right, value)

    """  
    
    def traverse(self, temp = None):
        result = []
        
        if temp == None:
            temp = self.root

        self.traverse_recurr(temp, result)

        return result

    def traverse_recurr(self, temp, result):
        if temp == None:
            return None

        else:
            # # pre-order
            # result.append(temp)
            # self.traverse_recurr(temp.left)
            # self.traverse_recurr(temp.right)

            # in-order
            self.traverse_recurr(temp.left, result)
            result.append(temp)
            self.traverse_recurr(temp.right, result)

            # # post-order
            # self.traverse_recurr(temp.left, result)
            # self.traverse_recurr(temp.right, result)
            # result.append(temp)
            
    '''

    # pre-order
    def __iter__(self):
        self.queue = [self.root]

        return self

        # OR
        # return iter(self.traverse())

    def __next__(self):
        if self.queue != []:
            x = self.queue.pop()

            if x.right != None:
                self.queue.append(x.right)

            if x.left != None:
                self.queue.append(x.left)

            return x
        
        else:
            raise StopIteration
        
    '''




# Testing

node1 = Node(50)
node2 = Node(30)
node3 = Node(70)
node4 = Node(10)
node5 = Node(40)    
node6 = Node(30)
node7 = Node(75)
node8 = Node(60)
node9 = Node(100)



node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node8
node3.right = node7

node7.right = node9




bst = BST(node1)

for i in bst.traverse():
    print(i.item)

print()

print(bst.insert(0))


for i in bst.traverse():
    print(i.item)
    
print()

bst.delete(10)

for i in bst.traverse():
    print(i.item)
    
print()




