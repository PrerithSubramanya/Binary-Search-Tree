def find_element(initial_node,element):
    while initial_node is not None: # when root is not none 
        if initial_node.get_data() == element: # if the element is found 
            print("element found", element)
            break
        elif initial_node.get_data() > element: # search left 
            initial_node = initial_node.get_left()
        elif initial_node.get_data() < element: # search right
            initial_node = initial_node.get_right()
    else:   
        print("element not found", element) # if element not found
