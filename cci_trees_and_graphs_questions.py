from math import floor
"""
4.1) Given a directed graph, design an algorithm to find out whether there is a
     route between two nodes.
"""
#Assuming that the graph is represented as a hash table.
def route(graph, start, destination):
    #Time Comlexity = O(1), Space Complexity = O(1)
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
        self.parent = None #Needed for question 4.6

class Binary_Search_Tree():
    def __init__(self, data):
        self.root = Node(data)
        
    def insert(self, data):
        pass
    
    def find(self, data):
        node = self.root
        queue = [node]
        nodes = [] #Holds nodes with data equal to data value we are searching for.
        
        while len(queue) > 0:
            node = queue.pop()
            
            if node.data == data:
                nodes.append(node)
                
                #Assuming nodes that are equal to its parent are store as a right child.
                #Only add the right child if it is equal to the data we are looking for
                #this will prevent us from looking through unnecessary nodes.
                if not node.right_child == None:
                    if node.right_child.data == data:
                        queue.append(node.right_child) 
                
            if data < node.data:
                #Add left_child to the queue if it exist
                if not node.left_child == None:
                    queue.append(node.left_child)
        
            if data > node.data:
                #Add right_child to the queue if it exist
                if not node.right_child == None:
                    queue.append(node.right_child)
        
        if len(nodes) == 0:
            return None
        else:
            return nodes
    
    def delete(self, data):
        pass

def create_minimal_tree(array):
    #Time Complexity = O(N), Space Complexity = O(N)
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
        
        #Set the left sub tree roots parent (Needed for question 4.6)
        left_sub_tree.root.parent = tree.root
    else:
        tree.root.left_child = None
    
    #Create a binary search tree with the right partition.
    right_sub_tree = create_minimal_tree(right)
    if right_sub_tree != None:
        #Set the root's right_child = right_sub_tree's root
        tree.root.right_child = right_sub_tree.root
        
        #Set the right sub tree roots parent (Needed for question 4.6)
        right_sub_tree.root.parent = tree.root 
    else:
        tree.root.right_child = None
    
    return tree
    
def partition(array):
    #Time Complexity = O(c), Space Complexity = O(N)
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
    #Time Complexity = O(N), Space Complexity = O(N)
    if root == None:
        return nodes_at_depth
    
    # Append the this nodes data to the list at this depth. If the list does 
    # not exist for this depth, create it then append this nodes data to it.
    try:
        nodes_at_depth[depth].append(root.data)
    except IndexError:
        nodes_at_depth.append([root.data])
    
    # Add the left childs and right childs data to the next depth's (depth+1)
    # list.
    lists_of_depth(root.left_child, depth+1, nodes_at_depth)
    lists_of_depth(root.right_child, depth+1, nodes_at_depth)
    
    return nodes_at_depth
        
"""
4.4) Implement a function to check if a binary tree is balanced. For the 
     purposes of this question, a balanced tree is defined to be a tree such 
     that the heights of the two subtrees of any node never differ by more 
     than one.
"""
def check_balance(root):
    #Time Complexity = O(N), Space Complexity = O(C)
    if root == None:
        return False
    
    left_height = get_height(root.left_child)
    right_height = get_height(root.right_child)
    
    if abs(left_height - right_height) > 1:
        return False
    else:
        return True
    
def get_height(root, height=0):
    #Time Complexity = O(N), Space Complexity = O(C)
    
    #If the root of the tree is None then it has no height, return 0 
    if root == None:
        return height
    
    height += 1
    
    #To avoid additional calls only call the function for children the are not 
    #equal to None.
    if root.left_child != None:
        left_height = get_height(root.left_child, height)
    else:
        #If the child is None the total height of the tree will not increase.
        left_height = height
    
    if root.right_child != None:
        right_height = get_height(root.right_child, height)
    else: 
        right_height = height
    
    #Return the height of the tallest subtree.
    if left_height > right_height:
        return left_height
    else:
        return right_height
    
    
"""
4.5) Implement a function to check if a binary tree is a binary search tree.
"""
def valid_BTS(root):
    #Time Complexity = O(N), Space Complexity = O(2^d) where d is the depth of 
    #the tree
    if root == None:
        return False
    
    queue = [root]
    
    while len(queue) > 0:
        node = queue.pop()
        
        #If the left_child is not a NoneType and is less than its parent add it
        #to the queue.
        if node.left_child == None:
            #Do nothing
            pass
        elif node.left_child.data > node.data:
            return False
        else:
            queue.append(node.left_child)
        
        #If the right_child is not a NoneType and is greater than its parent
        #add it to the queue.
        if node.right_child == None:
            #Do nothing
            pass
        elif node.right_child.data < node.data:
            return False
        else:
            queue.append(node.right_child)
           

    return True 

"""
4.6) Write an algorithm to find the "next" node (i.e., in-order successor) of 
     a given node in a binary search tree. You may assume that each node has a 
     link to its parent

                                 20 <-- When passed returns None ✔
                                / 
                               7 <-- When passed returns 8 ✔
                              / \
✔ When passed returns 7 --> 5   8 <-- When passed returns 9 ✔
                                  \
                                   9 <-- When passed returns 20 ✔
"""
def successor(node, check_right=True):
    #Time Complexity = O(k+1) where k is the depth at the starting node.
    #Space Complexity = O(C)
    
    #First check if the starting node has a right child, if it does then the 
    #right child is the successor. If there is no right child then we search 
    #for and return an ancestor that is greater than its decendents. If none 
    #exist then the starting node is the largest node in the tree. These 
    #assumption only work for BST's.
    if node == None:
        return None
    
    if check_right: #Only check the right on the first iteration.
        if node.right_child != None:
            return node.right_child.data
    
    if node.parent == None: #Assuming each node has a link to the parent.
        return None
    
    if node.parent.data > node.data:
        return node.parent.data
    
    if node.parent.data < node.data:
        return successor(node.parent, check_right=False)
    
    
"""
4.7) Implement a function to check if a binary tree is balanced. For the 
     purposes of this question, a balanced tree is defined to be a tree such 
     that the heights of the two subtrees of any node never differ by more than
     one.
     
     projects = ['a','b','c','d','e','f']
     dependencies = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
     Expected Output: ['e', 'f', 'a', 'b', 'd', 'c']
"""
def build_order(projects, dependencies):
    #Time Compelxity = O(N(N+1)/2 x M(M+1)/2), Space Complexity = O(N)
    #TODO: Find a solution with a better time complexity.
    output = [] #Used to hold correct order.
    
    # When we add a project to the output we will remove it from the projects 
    # list. Continue until the projects list is empty.
    while len(projects) > 0: 
        # For each project in projects
        for project in projects:
            # Check each dependency to see if the project is dependent on 
            # another project.
            for dependency in dependencies:
                if project == dependency[1]:
                    # If the project is dependent on another set dependent
                    # equal to True.
                    dependent = True
                    break
                dependent = False
                
            # If the project is independent append it to the output and remove
            # it from projects
            if not dependent:
                output.append(project)
                projects.remove(project)
                update_dependencies(dependencies, project)
    
    return output

def update_dependencies(dependencies, project):
    #Time Complexity = O(N), Space Complexity = O(C)
    for dependency in dependencies:
        if project == dependency[0]:
            dependencies.remove(dependency)    
            
"""
4.8) Design an algorithm and write code to find the first common ancestor of 
     two nodes in a binary tree. Avoid storing additional nodes in a data 
     structure. NOTE: This is not necessarily a binary search tree.
"""
def first_common_ancestor(node1, node2):
    #Time Complexity = O(d) where d is the depth of the tree.
    #Space Complexity = O(d)
    if node1 == None or node2 == None:
        return None
    
    #Add all of node1's ancestors to a dict.
    ancestors = {}  #Dict to hold ancestors of node1.
    parent = node1.parent
    while not parent == None:
        #Add the parent to the dict.
        ancestors[parent] = 1
        #Get the next parent
        parent = parent.parent
    
    #Check node2's lineage until a common ancestor is found.
    parent = node2.parent
    while not parent == None:
        if parent in ancestors:
            return True
        else:
            #Get next parent
            parent.parent
    
    #The root is an ancestor of all nodes. Therefore if no ancestor is found 
    #then the nodes are not from the same tree. Return None.
    return None
                
"""
4.9) A binary search tree was created by traversing through an array from left 
     to right and inserting each element. Given a binary search tree with 
     distinct elements, print all possible arrays that could have led to this
     tree.
"""
def BST_sequences(root):
    sequences = []
    has_left = False
    has_right = False
    
    #If this node is a leaf node return the nodes data as a list in a list.
    if root.left_child == None and root.right_child == None:
        return [[root.data]]
    
    #If there is a left child get the left sub tree's sequences.
    if not root.left_child == None:
        has_left = True
        left_sequences = BST_sequences(root.left_child)
        
    #If there is a right child get the right sub tree's sequences.
    if not root.right_child == None:
        has_right = True
        right_sequences = BST_sequences(root.right_child)
    
    #Add this nodes data to the beginning of every possible left and right 
    #sequence combination.
    if has_left and has_right:
        for left in left_sequences:
            for right in right_sequences:
                sequences.append([root.data]+left+right)
                
        for right in right_sequences:
            for left in left_sequences:
                sequences.append([root.data]+right+left)
    
    #If there is no left node then only add this nodes data to the beginning of
    #of the right sub tree's sequences.
    if not has_left:
        #only add data to right
        for right in right_sequences:
            sequences.append([root.data]+right)
        
    if not has_right:
        #only add data to left
        for left in left_sequences:
            sequences.append([root.data]+left)
            
    return sequences

"""
4.10) Tl and T2 are two very large binary trees, with Tl much bigger than T2. 
      Create an algorithm to determine if T2 is a subtree of Tl.
      
      A tree T2 is a subtree of Tl if there exists a node n in Tl such that the
      subtree of n is identical to T2. That is, if you cut off the tree at node
      n, the two trees would be identical.
"""
#TODO: fix find it is not working for leaf nodes.
def check_subtree(t1, t2):
    #Time Complexity = O(), Space Complexity = O()
    #Find all nodes in t1 that have a value equal to t2.data.
    nodes = t1.find(t2.data)
    
    #If there are no nodes with values equal to t2.data return False
    if nodes == None:
        return False
    
    #Check if any of the nodes are equal to t2
    for node in nodes:
        if node == t2:
            return True
    
    return False
