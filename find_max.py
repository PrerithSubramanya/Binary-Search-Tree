# find max element in a BST

def find_max(rootNode):
    while rootNode.get_data() is not None: # when root is not none 
        if rootNode.get_right() is None: # serach the right most nodes untill none to find max
            print("Max element is ",rootNode.get_data())
            break
        else:
            rootNode = rootNode.get_right()
    else:
        print("No elements in BST")
