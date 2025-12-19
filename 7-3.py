class PriorityQueue:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.pre = None
            
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, x):
        node = self.Node(x)
        
        if self.head == None: # empty queue
            self.head = self.tail = node
                    
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
    
    def pop(self):
        min_index = self.head
        p = self.head
        
        while(p != None):
            if(p.data < min_index.data):
                min_index = p
            p = p.next
            
        if min_index.pre != None:
            min_index.pre.next = min_index.next
        else:
            self.head = min_index.next
            
        if min_index != self.tail:
            min_index.next.pre = min_index.pre
        else:
            self.tail = min_index.pre
        
        return min_index.data

pq = PriorityQueue()

pq.push(5)
pq.push(3)
pq.push(9)
pq.push(1)
print(pq.pop())
print(pq.pop())
print(pq.pop())
print(pq.pop())            
    