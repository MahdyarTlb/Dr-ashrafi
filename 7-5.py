class Stack:
    
    class Node:
        
        def __init__(self, data):
            self.data = data
            self.next = None
            
    def __init__(self):
        self.top = None
    
    def push(self, x):
        new_node = self.Node(x)
        
        new_node.next = self.top
        self.top = new_node
        
        print(f"pushed {x}")
        
    def pop(self):
        
        if self.top is None:
            print("empty!")
            return None
        
        x = self.top.data    
        self.top = self.top.next
        
        print(x)
    
    def peek(self):
        if not self.top is None:
            x = self.top.data
            return x
        return None