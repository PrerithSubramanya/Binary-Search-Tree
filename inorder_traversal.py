# to print the numbers in sorted order read the BST via inorder traversal method


def inorder_traversal(rootNode): # traverse left most node, visit node or root , traverse right node
    sorted_list =[] # to store elements in sorted order 
    stack = [] #to store and traverse from left subtree and then visit node
    while rootNode or stack: # loop to visit all nodes hence order of 'n' O(n)
        if  rootNode is not None:
            stack.append(rootNode)
            rootNode = rootNode.get_left()
        elif rootNode is None:
            rootNode = stack.pop()
            sorted_list.append(rootNode.get_data())
            rootNode = rootNode.get_right()
    
    for i in sorted_list:
        print(i)
