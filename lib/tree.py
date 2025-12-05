class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def get_element_by_id(self, id, method='dfs'):
        """Find a node by its id using specified traversal method.
        
        Args:
            id: The id to search for
            method: 'dfs' for depth-first or 'bfs' for breadth-first
        """
        if method == 'dfs':
            return self._depth_first_search(self.root, id)
        elif method == 'bfs':
            return self._breadth_first_search(self.root, id)
        else:
            raise ValueError("Method must be 'dfs' or 'bfs'")
    
    def _depth_first_search(self, node, target_id):
        """Depth-first search implementation."""
        if node is None:
            return None
        
        # Check if current node matches the target id
        if node.get('id') == target_id:
            return node
        
        # Recursively search through children
        for child in node.get('children', []):
            result = self._depth_first_search(child, target_id)
            if result is not None:
                return result
        
        return None
    
    def _breadth_first_search(self, node, target_id):
        """Breadth-first search implementation."""
        if node is None:
            return None
        
        # Initialize queue with root node
        nodes_to_visit = [node]
        
        while nodes_to_visit:
            # Remove first node from queue
            current_node = nodes_to_visit.pop(0)
            
            # Check if current node matches the target id
            if current_node.get('id') == target_id:
                return current_node
            
            # Add children to the end of the queue
            for child in current_node.get('children', []):
                nodes_to_visit.append(child)
        
        return None