def insert_node(root, node): # inserting a node
    if root is None:
        root = node #initalize root if root is none
    else:
        if root.get_data() > node.get_data(): # check for node data and push it either to left or right node
            if root.left_node is None:
                root.left_node = node
            else:
                insert_node(root.get_left(), node)
        if root.get_data() < node.get_data():
            if root.right_node is None:
                root.right_node = node
            else:
                insert_node(root.get_right(), node)
