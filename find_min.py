# find min element in a BST

def find_min(rootNode):
    while rootNode.get_data() is not None: # when root is not none 
        if rootNode.get_left() is None: # serach the left most nodes untill none to find min
            print("Min element is",rootNode.get_data())
            break
        else:
            rootNode = rootNode.get_left()
    else:
        print("No elements in BST")
