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
class Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class Binary_Search_Tree():
    def __init__(self, data):
        self.root = Node(data)

def create_minimal_tree(array):
    if array == None:
        return None
    
    #Partition the array 
    left, midpoint, right = partition(array)
    
    #Create a binary search tree with the midpoint being the root
    tree = Binary_Search_Tree(midpoint)

    #Create a binary search tree with the left partition.
    left_sub_tree = create_minimal_tree(left)
    if left_sub_tree != None:
        #Set roots left child = left sub tree root
        tree.root.left_child = left_sub_tree.root
    else:
        tree.root.left_child = None
    
    #Create a binary search tree with the right partition.
    right_sub_tree = create_minimal_tree(right)
    if right_sub_tree != None:
        #Set the root's right_child = right_sub_tree's root
        tree.root.right_child = right_sub_tree.root
    else:
        tree.root.right_child = None
    
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
    
"""
4.3) Given a binary tree, design an algorithm which creates a list of 
     all the nodes at each depth (e.g., if you have a tree with depth D, you'll
     have D lists).
"""

def lists_of_depth(root, depth=0, nodes_at_depth=[]):
    if root == None:
        return nodes_at_depth
    
    # Append the this nodes data to the list at this depth. If the list does 
    # not exist create it then append this nodes data to it.
    try:
        nodes_at_depth[depth].append(root.data)
    except IndexError:
        nodes_at_depth.append([root.data])
    
    # Add the left childs and right childs data to the next depth's (depth+1)
    # list.
    nodes_at_depth = lists_of_depth(root.left_child, depth+1, nodes_at_depth)
    nodes_at_depth = lists_of_depth(root.right_child, depth+1, nodes_at_depth)
    
    return nodes_at_depth
        
    
