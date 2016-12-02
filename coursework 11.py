""" Based on the Python code or the C++ code provided in class as a starting point, implement the double linked listnode delete function. """
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self,n,x):
        if n != None:
            x.next = n.next
            n.next = x
            x.prev = n
        if x.next != None:
            x.next.prev = x              
        if self.head == None:
            self.head = self.tail = x
            x.prev = x.next = None
        elif self.tail == n:
            self.tail = x
            
    def delete(self, n):
        """ deleting a node, first search for the node to be deleted """
        current = self.head
        result = None
        while result is None:
            if current.value == n:
                result = current
            current = current.next
        """ decision tree for what to do based on where the element is in the list
            was the node the head, in the middle or at the end
        """
        if result.prev != None:
            result.prev.next = result.next
        else:
            self.head = result.next
        if result.next != None:
            result.next.prev = result.prev
        else:
            self.tail = result.prev
            
    def display(self):
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print ("List:",",".join(values))
