class graph_adj_matrix:
    def __init__(self, vno):
        self.vno = vno
        self.adj_matrix = [ [0]*vno for e in range(vno)]

    def add_edge(self, vertex1, vertex2, weight = 1):
        if 0 <= vertex1 < self.vno and 0 <= vertex2 < self.vno:
            self.adj_matrix[vertex1][vertex2] = weight
            self.adj_matrix[vertex2][vertex1] = weight

        else:
            print("Invalid Vertex")

    def remove_edge(self, vertex1, vertex2):
        if 0 <= vertex1 < self.vno and 0 <= vertex2 < self.vno:
            self.adj_matrix[vertex1][vertex2] = 0
            self.adj_matrix[vertex2][vertex1] = 0

        else: 
            print("Invalid Vertex")

    def has_edge(self, vertex1, vertex2):
        if 0 <= vertex1 < self.vno and 0 <= vertex2 < self.vno:
            if self.adj_matrix[vertex1][vertex2] != 0:
                return True
            
        return False
        

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            l = map(str, row_list)
            
            print(" ".join(l))




class graph_adj_lst:
    def __init__(self, vno):
        self.adj_lst = dict([(i, []) for i in range(vno)])
        self.vno = vno

    def add_edge(self, vertex1, vertex2, weight = 1):
        if 0 <= vertex1 < self.vno and 0 <= vertex2 < self.vno:
            self.adj_lst[vertex1].append((vertex2, weight))
            self.adj_lst[vertex2].append((vertex1, weight))

        else:
            print("Invalid Vertex")

    def remove_edge(self, vertex1, vertex2, weight = 1):
        if 0 <= vertex1 < self.vno and 0 <= vertex2 < self.vno:
            if self.has_edge(vertex1, vertex2, weight):
                self.adj_lst[vertex1].remove((vertex2, weight))
                self.adj_lst[vertex2].remove((vertex1, weight))
            else:
                print("No such Edge")

            """
            OR

            self.adj_lst[vertex1] = [(vertex, weight) for vertex, weight in self.adj_list[vertex1] if vertex != vertex2]
            self.adj_lst[vertex2] = [(vertex, weight) for vertex, weight in self.adj_list[vertex2] if vertex != vertex1]
            """

        else: 
            print("Invalid Vertex")

    def has_edge(self, vertex1, vertex2, weight = 1):
        if 0 <= vertex1 < self.vno and 0 <= vertex2 < self.vno:
            # if (vertex2, weight) in self.adj_lst[vertex1]:
            #     return True

            # Or

            return any(vertex == vertex2 and weight == weight for vertex, _ in self.adj_lst[vertex1])
            
        return False
        

    def print_adj_matrix(self):
        
        for i in self.adj_lst:
            print("V", i, " : ", self.adj_lst[i])

    
    

    

# Testing

grf = graph_adj_lst(5)

grf.add_edge(0, 2)
grf.add_edge(0, 4)
grf.add_edge(1, 2)
grf.add_edge(4, 3)
grf.add_edge(3, 1)

grf.remove_edge(0, 4)

print(grf.has_edge(0, 1))

grf.print_adj_matrix()