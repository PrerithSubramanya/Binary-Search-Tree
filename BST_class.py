class BSTnode: # basic frame of a binary search tree
    def __init__(self,data): #constructor
        self.data = data  #node value 
        self.left_node = None   #left node value
        self.right_node = None  # right node value
        
    def get_data(self):
        return self.data
    
    def get_left(self):  #left node value getter
        return self.left_node
    
    def get_right(self): #right node value getter
        return self.right_node
