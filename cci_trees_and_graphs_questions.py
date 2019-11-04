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

