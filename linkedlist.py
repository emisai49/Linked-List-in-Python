class Node:
    def __init__ (self,data):
       self.data = data
       self.next = None
       
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)
        
#Test code: they should print out the same thing
#n = Node(10)
#print str(n)
#print repr(n)
#print n

class LinkedList:
    def __init__(self, data):
        first_node = Node(data)
        self.first = first_node
        self.last = first_node
        self.n = 1
        self.current = first_node
        
    def append(self, appdata):
        node2 = Node(appdata)
        self.last.next = node2
        self.last = node2
        self.n += 1

# Implementation without using generator
#    def __iter__(self):
#        return self
#    
#    def next(self):
#        # if the current node is none
#        if self.current == None:
#            self.current = self.first
#            raise StopIteration
#        else:
#            # use the temp to store the current node info, since we would like to return it later
#            temp = self.current
#            # iterate the node to the next node
#            self.current = self.current.next
#            # return the data of the current node 
#            return temp.data

# Implementation with generator
    def __iter__(self):
        return self.generator()
    
    def generator(self):
        self.current = self.first
        while self.current:
            yield self.current.data
            self.current = self.current.next
 
# Implementation of some magic methods
    def __len__(self):
        return self.n
    
    def __str__(self):
        final = "["
        node_now = self.first
        while not node_now == None:
            final += str(node_now.data) + "->"
            node_now = node_now.next
        final += "]"
        return final
            
    def __repr__(self):
        final = "["
        node_now = self.first
        while not node_now == None:
            final += repr(node_now.data) + "->"
            node_now = node_now.next
        final += "]"
        return final
    
    def __getitem__ (self, num):
        if num > self.n -1 or num < 0 or type(num) is not int:
            raise IndexError
            return "Warning! Index is out of bouondary."
        else:
            index = 0
            node_change = self.first
            while index < num:
                node_change = node_change.next
                index += 1
            return node_change.data
        
    def __setitem__(self, num, value):
        if num > self.n -1 or num < 0 or type(num) is not int:
            raise IndexError
        else:
            index = 0
            node_change = self.first
            while index < num:
                node_change = node_change.next
                index += 1
            node_change.data = value
            return 
        
    def __add__(self, data):
        #create an empty LinkedList
        emptyll = LinkedList (self.first.data)
        #set the node to the first node in the orignial linkedlist
        copynode = self.first.next
        while not copynode == None:
            emptyll.append(copynode.data)
            copynode = copynode.next
        emptyll.append(data)
        return emptyll

             
# Still thinking about this part. Trying to implement __getitem__ for slicing.
#  def __getitem__(self, start, end, by):
#
