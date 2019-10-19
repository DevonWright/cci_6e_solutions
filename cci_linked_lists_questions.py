class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_node):
        self.next_node = new_node
        

class LinkedList(object):
    
    def __init__(self, head=None):
        self.head=head
        
    def append_head(self, data):
        #Time Complexity = O(1)
        new_head = Node(data, self.head)
        self.head = new_head
        
    def append_tail(self, data):
        #Time Complexity = O(N) where N is the length on the linked list
        new_tail = Node(data)
        current_node = self.head
        
        while(current_node.get_next() is not None):
            current_node = current_node.get_next()
        
        current_node.set_next(new_tail)
        
        

"""
2.1) Write code to remove duplicates from an unsorted linked list.
"""
def remove_dups(linked_list):
    table = {}
    n = linked_list.head
    while(n.next != None):
        if n.data in table:
            n.prev.next = n.next
        else:
            table[n.data] = 1
        n = n.next
    
    if n.data in table:
        n.prev.next = n.next
    
    return linked_list.head



"""
2.2) Implement an algorithm to find the kth to last element of a singly linked 
     list.
"""

def kth_last(linked_list, k):
    length = 1
    n = linked_list.head
    while n.next != None:
        n = n.next
        length += 1
    
    n = linked_list.head
    for i in range(0,length-k):
        
        n.next
    return n


"""
2.3) Implement an algorithm to delete a node in the middle (i.e., any node but
     the first and last node, not necessarily the exact middle) of a singly 
     linked list, given only access to that node.
"""

def delete_node(n):
    if n == None or n.next == None:
        return False
    else:
        n.data = n.next.data
        n.next = n.next.next
        return True



"""
2.4) Write code to partition a linked list around a value x, such that all 
     nodes less than x come before all nodes greater than or equal to x. If x 
     is contained within the list, the values of x only need to be after the 
     elements less than x (see below). The partition element x can appear 
     anywhere in the "right partition"; it does not need to appear between the 
     left and right partitions.
"""

def partition(head, partition):
    greater = LinkedList()
    less = LinkedList()
    
    node = head
    
    while node != None:
        if node.data == partition:
            # Make node.data the new head of greater
            pass
        if node.data < partition:
            # Make node.data the new head of less
            pass
        else:
            # Append node.dat to the end of greater
            pass
        node = node.next
            
    if less.head != None and greater.head != None:
        less.appendToTail(greater.head)
        return less.head
    elif less.head == None:
        return greater.head
    elif greater.head == None:
        return less.head
        


"""
2.5) You have two numbers represented by a linked list, where each node 
     contains a single digit. The digits are stored in reverse order, such that
     the 1 's digit is at the head of the list. Write a function that adds the 
     two numbers and returns the sum as a linked list.  
"""

def sum_lists(ll1, ll2):
    node1 = ll1.head
    node2 = ll2. head
    multiplier = 1
    sum = 0 
    
    while node1 != None:
        sum += (node1 + node2) * multiplier
        multiplier *= 10
        node1 = node1.next
        node2 = node2.next
    return sum

def sum_lists_reverse(ll1, ll2):
    node1 = ll1.head
    length = 0
    while node1 != None:
        length += 1
    
    multiplier = 10 ** length
    node1 = ll1.head
    node2 = ll2.head
    sum = 0
    
    while node1 != None:
        sum += (node1 + node2) * multiplier
        multiplier *= 10
        node1 = node1.next
        node2 = node2.next
    return sum


"""
2.7) Given two (singly) linked lists, determine if the two lists intersect.
    Return the intersecting node. Note that the intersection is defined based 
    on reference, not value. That is, if the kth node of the first linked list
    is the exact same node (by reference) as the jth node of the second linked
    list, then they are intersecting.
"""

def intersecting(ll1, ll2):
    ll1_dict = to_dict(ll1)
    return check_intersection(ll1_dict, ll2)
    
    
def to_dict(linked_list):
    ll1_dict = {}
    node = linked_list.head()
    while node != None:
        if node.data in ll1_dict:
            ll1_dict[node.data] = ll1_dict[node.data], node
        else:
            ll1_dict[node.data] = node
    return ll1_dict

def check_intersection(ll1_dict, ll2):
    node = ll2.head
    while node != None:
        if node.data in ll1_dict:
            for value in ll1_dict[node.data]:
                if value == node:
                    return node
    return False