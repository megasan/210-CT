class Graph(object):

    def __init__(self, graph={}):
        """ create the graph dictionary. use empty dictionary if no input. """
        self.graph = graph

    def vertex(self, v):
        """ add new vertex. checks to see if vertex is already present before adding. """
        if v not in self.graph:
            self.graph[v] = []
            
    def vertices(self):
        """ returns vertices of graph, the keys of the dictionary, as list. """
        return list(self.graph.keys())
        
    def edge(self, edge):
        """ edge data is in format vertex 1, vertex 2, weight. checks to see if origin vertex is present before adding. """
        (v1, v2, w) = tuple(edge)
        if v1 in self.graph:
            self.graph[v1].append([v2,w])
            
    def adjacency(self):
        return sorted(self.graph)

    def edges(self):
        """ return the edges connecting vertices. list of edges, """
        edges = []
        for v1 in self.graph:
            for v2 in self.graph[v1]:
                if [v2, v1] not in edges:
                    edges.append([v1, v2])
        return sorted(edges)

def dfs(graph, start):
    """ depth first search. uses a stack, first in last out. """
    x = graph.edges()
    path = []
    stack = [start]
    """ while there are elements in the stack, if the vertex has not been visited, add it to the visited list and remove it from the stack. if the vertex has any edges look in the edges and add destination nodes to the stack. repeat until there are no more items in the stack. """
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for i in x:
                if v in i:
                    stack.append(i[1][0])
    return visited

def bfs(graph, start):
    """ breadth first search. uses a queue, first in first out.  """
    x = graph.edges()
    path = []
    queue = [start]
    """ while there are elements in the queue, if the vertex has not been visited, add it to the visited list and remove it from the queue. if the vertex has any edges look in the edges and add destination nodes to the queue. repeat until there are no items in the queue. """
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            for i in x:
                if v in i:
                    queue.append(i[1][0])
    return visited
    
""" write to file """
def save_file(graph, start):
    f = open('search.txt','w')
    f.write("DFS: ")
    f.write(str(dfs(graph, start)))
    f.write("\n")
    f.write("BFS : ")
    f.write(str(bfs(graph, start)))
    f.close()
