"""binary_search_tree.py 
Exercises from chapter 6 section 6.7 'Binary Search Trees' of 
Miller &amp; Ranum "Problem Solving with Algorithms and Data Structures Using Python" (second edition)
""" 


class BinarySearchTree: 
    """ Binary Search Tree class
    Has a reference to the TreeNode that is the root of the binary search tree. 
    If there are nodes in the tree, the request is passed to a private method 
    that takes the root as a parameter. 
    """
    
    def __init__(self): 
        self.root = None 
        self.size = 0 

    def length(self): 
        return self.size 
    
    def __len__(self): 
        return self.size 
    
    def __iter__(self): 
        return self.root.__iter__() 
    
    

class TreeNode: 
    """ Tree Node class 
    Provides helper functions. Many help to classify a node 
    according to its own position as a left or right child, 
    and the kind of children the node has. 
    Registers the parent as an attribute of the node. 
    Optional parameters enable Tree Node construction under 
    various circumstances. 

    #TODO: handle the insertion of a duplicate key by replacing 
    old value with new. 
    """ 

    # initialise 
    def __init__(self, key, val, left=None, right=None, parent=None): 

        self.key = key 
        self.payload = val 
        self.left_child = left 
        self.right_child = right 

    def has_left_child(self): 
        return self.left_child 

    def has_right_child(self): 
        return self.right_child 

    def is_left_child(self): 
        return (self.parent and self.parent.left_child == self) 

    def is_right_child(self): 
        return (self.parent and self.parent.right_child == self) 

    def is_root(self): 
        return (not self.parent) 

    def is_leaf(self): 
        return (not (self.right_child or self.left_child))

    def has_any_children(self): 
        return (self.right_child or self.left_child) 

    def has_both_children(self): 
        return (self.right_child and self.left_child) 
    
    def replace_node_data(self, key, value, lchild, rchild): 
        self.key = key 
        self.payload = value 
        self.left_child = lchild
        self.right_child = rchild 
        if self.has_left_child(): 
            self.left_child.parent = self 
        if self.has_right_child(): 
            self.right_child.parent = self 


    
    # getters and setters 

    def put(self, key, val): 
        if self.root: 
            self._put(key, val, self.root) 
        else: 
            self.root = TreeNode(key, val) 
        self.size = self.size + 1 

    def _put(self, key, val, current_node): 
        
        if key < current_node.key: 
            if current_node.has_left_child(): 
                self._put(key, val, current_node.left_child) 
            else: 
                current_node.left_child = TreeNode(key, val, parent = current_node)
        
        else: 
            if current_node.has_right_child(): 
                self._put(key, val, current_node.right_child) 
            else: 
                current_node.right_child = TreeNode(key, val, parent = current_node) 

    def __setitem__(self, k, v): 
        self.put(k, v) 
    
    def get(self, key): 
        if self.root: 
            res = self._get(key, self.root) 
            if res: 
                return res.payload 
            else: 
                return None 
        else: 
            return None 
    
    def _get(self, key, current_node): 
        if not current_node: 
            return None 
        elif current_node.key == key: 
            return current_node 
        elif key < current_node.key: 
            return self._get(key, current_node.left_child) 
        else:
            return self._get(key, current_node.right_child) 
        
    def __getitem__(self, key): 
        return self.get(key) 
    
    def __contains__(self, key): 
        if self._get(key, self.root): 
            return True 
        else: 
            return False 
    
    # deleting keys 
    def delete(self, key): 
        """
        First, search the tree to find the node to be deleted. 
        If the node is not the root use _get(). 
        If the key is not found del will raise an error. 
        """ 

        if self.size > 1: 
            purge_node = self._get(key, self.root) 
            if purge_node: 
                self.remove(purge_node) 
                self.size = self.size -1 
            else: 
                raise KeyError("Error, key not in tree") 
        
        elif self.size == 1 and self.root.key == key: 
            self.root = None 
            self.size = self.size -1 
        else: 
            raise KeyError("Error, key not in tree") 
        
    def __delitem__(self, key): 
        self.delete(key) 


    # deleting a key 

    def remove(self, current_node): 
        """
        Scenarios: 
        1. When the purge node has no children, 
        delete the node and remove the left or right link to it 
        from the parent. 
        2. the purge node has only one child 
        3. When the purge node has two children 
        """ 

        if current_node.is_leaf(): # no children 
            if current_node == current_node.parent.left_child: 
                current_node.parent.left_child = None 
            else: 
                current_node.parent.right_child = None 
        
        elif current_node.has_both_children(): # two children  
            successor = current_node.find_successor() 
            successor.splice_out() 
            current_node.key = successor.key 
            current_node.payload = successor.payload 
        
        else: # one child 
            if current_node.has_left_child(): 
                if current_node.is_left_child(): 
                    current_node.left_child.parent = current_node.parent 
                elif current_node.is_right_child(): 
                    current_node.left_child.parent = current_node.parent 
                    current_node.parent.right_child = current_node.left_child 
                else: 
                    current_node.replace_node_data(
                        current_node.left_child.key, 
                        current_node.left_child.payload, 
                        current_node.left_child.left_child, 
                        current_node.left_child.right_child 
                    ) 
            else: 
                if current_node.is_left_child(): 
                    current_node.right_child.parent = current_node.parent 
                    current_node.parent.parent.left_child = current_node.right_child 
                elif current_node.is_right_child(): 
                    current_node.right_child.parent = current_node.parent 
                else: 
                    current_node.replace_node_data(
                        current_node.right_child.key, 
                        current_node.right_child.payload, 
                        current_node.right_child.left_child, 
                        current_node.right_child.right_child 
                    ) 

    
    def __iter__(self): 
        if self: 
            
            if self.has_left_child(): 
                for elementl in self.left_child: 
                    yield elementl 
            
            yield self.key 

            if self.has_right_child(): 
                for elementr in self.right_child: 
                    yield elementr 
    
    
    # Finding the Successor 

    def find_successor(self): 
        successor = None 
        if self.has_right_child(): 
            successor = self.right_child.find_min() 
        else: 
            if self.parent: 
                if self.is_left_child() : 
                    successor = self.parent 
                else: 
                    self.parent.right_child = None 
                    successor = self.parent.find_successor() 
                    self.parent.right_child = self 
        return successor
    

    # Splice out a Node 

    def splice_out(self): 
        """Goes directly to the node we want to splice out 
        and makes the change""" 

        if self.is_leaf(): 
            if self.is_left_child(): 
                self.parent.left_child = None 
            else: 
                self.parent.right_child = None 
        
        elif self.has_any_children(): 
            if self.has_left_child(): 
                if self.is_left_child(): 
                    self.parent.left_child = self.left_child 
                else: 
                    self.parent.right_child = self.left_child 
                self.left_child.parent = self.parent 
            else: 
                if self.is_left_child(): 
                    self.parent.left_child = self.right_child 
                else: 
                    self.parent.right_child = self.right_child 
                self.right_child.parent = self.parent 
                


  

        
