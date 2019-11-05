from math import floor
"""
4.1) Given a directed graph, design an algorithm to find out whether there is a
     route between two nodes.
"""
#Assuming that the graph is represented as a hash table.
def route(graph, start, destination):
    if graph[start] == None:
        return False
    elif destination in graph[start]:   
        return True 
    else:
        return False

"""
4.2) Given a sorted (increasing order) array with unique integer elements, 
     write an algorithm to create a binary search tree with minimal height.
"""
#TODO: Finish the Node and BTS classes.
class Node():
    pass

class Binary_Search_Tree():
    pass

def create_minimal_tree(array):
    if array == None:
        return None
    
    #Partition the array 
    left, midpoint, right = partition(array)
    
    #Create a binary search tree with the midpoint being the root
    tree = Binary_Search_Tree(midpoint)
    
    #Create a binary search tree with the left partition and make it the left child of the current tree.
    tree.root.left_child = create_minimal_tree(left).root
    
    #Create a binary search tree with the right partition and make it the left child of the current tree.
    tree.root.right_child = create_minimal_tree(right).root
    
    return tree
    
    
def partition(array):
    if len(array) == 1:
        #There is no left of right sides, just the midpoint.
        return None, array[0], None
    elif len(array) == 2:
        #There is no right side, just the midpoint and the left side.
        return array[0], array[1], None
    else:
        #Find the middle index
        middle_index = floor(len(array)/2) 
        
        #Partition the array into 3 parts
        left_side = array[:middle_index]
        right_side = array[middle_index + 1:]
        middle_element = array[middle_index]
        
        return left_side, middle_element, right_side
    
