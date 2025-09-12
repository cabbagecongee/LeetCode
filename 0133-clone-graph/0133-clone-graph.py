"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        start_node = node
        visited = {start_node: Node(start_node.val, [])} #original : clone
        #we will do bfs -> go through each layer sequentially
        q = []
        q.append(node)
        while q:
            node = q.pop(0)
            neighbors = node.neighbors
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[node].neighbors.append(visited[neighbor])
        return visited[start_node]
        
            
            

        


        