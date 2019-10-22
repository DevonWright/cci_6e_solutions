class Node():
    def __init__(self, data=None, next_node=None, past_min=None):
        self.data = data
        self.next_node = next_node
        self.past_min = past_min

class Stack():
    def __init__(self, top=None, minimum=None):
            self.top = top
            self.minimum = minimum
            self.count = 0  #Needed for SetOfStacks question.
            
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

    """
    3.2) How would you design a stack which, in addition to push and pop, has a 
         function min which returns the minimum element? Push, pop and min should 
         all operate in 0(1) time.
    """
    def min(self):
        """Returns the minimum element in the stack."""
        return self.minimum.data
  
              
"""
3.3) Imagine a (literal) stack of plates. If the stack gets too high, it might 
     topple. Therefore, in real life, we would likely start a new stack when 
     the previous stack exceeds some threshold. Implement a data structure 
     SetOfStacks that mimics this. SetO-fStacks should be composed of several 
     stacks and should create a new stack once the previous one exceeds 
     capacity. SetOfStacks. push() and SetOfStacks. pop() should behave 
     identically to a single stack (that is, pop () should return the same 
     values as it would if there were just a single stack).
"""
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
           
    """
    FOLLOW UP:
    Implement a function popAt (int index) which performs a pop operation on 
    a specific sub-stack.
    """
    def popAt(self, index):
        """Removes the node at the top of the stack at the index."""
        stackAtIndex = self.stacks[index]
        item = stackAtIndex.pop()
        if stackAtIndex.is_Empty():
            self.stacks.remove(stackAtIndex)
        return item


"""
3.4) Implement a MyQueue class which implements a queue using two stacks.
"""
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
    
"""
3.5) Write a program to sort a stack such that the smallest items are on the
     top. You can use an additional temporary stack, but you may not copy the 
     elements into any other data structure (such as an array). The stack 
     supports the following operations: push, pop, peek, and is Empty.
"""

#TODO: Stacks return node.data not the actual node. Fix sort.
def sort(stack):
    sorted = False
    largest = None
    prev_largest = None
    
    while not sorted:
        largest = find_largest(stack, prev_largest)
        stack, sorted = place_largest(stack, largest, prev_largest)
        prev_largest = largest
        
    return stack
    
def find_largest(stack, prev_largest):
    temp = Stack()
    largest = stack.peek()
    node = stack.pop()
    
    while node != prev_largest:
        if node.data > largest.data:    #ERROR: int does not have data attribute.
            largest = node
        temp.push(node)
        node = stack.pop()
        
    return largest

def place_largest(stack, largest, prev_largest):
    temp = Stack()
    node = stack.pop()
    
    #Retrive the largest node.
    not_retrieved = True
    while not_retrieved:
        if node == largest:
            not_retrieved = False
        else:
            temp.push(node)
            node = stack.pop
    
    #Place largest node on top of previous largest.
    not_placed = True
    while not_placed:
        if stack.peek() == prev_largest:
            stack.push(node)
            not_placed = False
        else:
            temp.push(stack.pop())
        
    #Push the temp stack back onto the main stack
    while not temp.is_Empty():
        stack.push(temp.pop())
        
    if stack.peek() == largest:
        return stack, True
    else: 
        return stack, False
