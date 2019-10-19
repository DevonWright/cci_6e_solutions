class MyQueue():
    """A queue data structure that is made up  of two stacks."""
    def __init__(self):
        self.main = Stack()
        self.buffer = Stack()
        
    def add(self, data):
        """Adds a node to the end of the queue."""
        self.main.push(data)
    
    def remove(self):
        """Removes the node at a the beginning of the queue."""
        #Pop all the items from the main stack onto the buffer stack.
        while not self.main.is_Empty():
            self.buffer.push(self.main.pop())
        
        #The item at the top of the buffer stack is at the beginning of the queue.
        item = self.buffer.pop()
        
        #Pop all the elements in the buffer stack back onto the main stack.
        while not self.buffer.is_Empty():
            self.main.push(self.buffer.pop())
            
        return item
    
    def peek(self):
        """Returns the node at the beginnning of the queue but does not remove it."""
        #Pop all the items from the main stack onto the buffer stack.
        while not self.main.is_Empty():
            self.buffer.push(self.main.pop())
        
        #The item at the top of the buffer stack is at the beginning of the queue.
        item = self.buffer.top.data
        
        #Pop all the elements in the buffer stack back onto the main stack.
        while not self.buffer.is_Empty():
            self.main.push(self.buffer.pop())
            
        return item
    
    def is_Empty(self):
        """Returns True if the queue is empty."""
        return self.main.is_Empty()

class SetOfStacks():
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.current = Stack()
        self.stacks = [self.current]
        
    def push(self, data):
        """Adds a node onto the top of the current stack."""
        if self.current.count == self.capacity:
            self.current = Stack()
            self.stacks.append(self.current)
        self.current.push(data)
            
    def pop(self):
        """Removes the node at the top of the stack."""
        item = self.current.pop()
        if self.current.is_Empty():
            self.stacks.remove(self.current)
            self.current = self.stacks[len(self.stacks)-1]
        return item
            
    def popAt(self, index):
        """Removes the node at the top of the stack at the index."""
        stackAtIndex = self.stacks[index]
        item = stackAtIndex.pop()
        if stackAtIndex.is_Empty():
            self.stacks.remove(stackAtIndex)
        return item
        
        
class Stack():
    def __init__(self, top=None, minimum=None):
            self.top = top
            self.minimum = minimum
            self.count = 0
            
    def pop(self):
        """Removes the node at the top of the stack."""
        try:
            if self.top == None:
                raise AttributeError
            elif self.top == self.minimum:
                self.minimum = self.top.past_min
            item = self.top.data
            self.top = self.top.next_node
            self.count -= 1
            return item
        except AttributeError:
            print('Stack is empty.')
        
    def push(self, data):
        """Adds a node onto the top of the stack."""
        new_node = Node(data, self.top)
            
        if self.top == None:
            self.minimum = new_node
        elif new_node.data < self.minimum.data:
            new_node.past_min = self.minimum
            self.minimum = new_node
        self.top = new_node
        self.count += 1
            
    def peek(self):
        """Returns the node at the top of the stack, but does not remove it."""
        try: 
            if self.top == None:
                raise AttributeError
            else:
                item = self.top.data
                return item
        except AttributeError:
            print('Stack is empty.')
                
    def is_Empty(self):
        """Returns True if the stack is empty."""
        if self.top == None:
            return True
        else:
            return False
            
    def min(self):
        """Returns the minimum element in the stack."""
        return self.minimum.data
    
    
class Node():
    def __init__(self, data=None, next_node=None, past_min=None):
        self.data = data
        self.next_node = next_node
        self.past_min = past_min
                
    