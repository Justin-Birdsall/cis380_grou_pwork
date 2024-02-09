# Authors: Richard Roy, Justin Birdsall

class sat_tree_node:
    def __init__(self, data):
        self.data = data
        self.children = {}  # dictionary of children, each is a branch 
                            # with the next satellite being any of the 
                            # satellites in the list that are left
                            # to enumerate all paths
                            # we will need to traverse the tree
                            # and the number of times we traverse the tree
                            # needs to be the number of satellites
                            # so we know we have a valid path
                            
        self.total_energy = 0      # energy
                            
# helper function to help us enumerate all paths
# (all branches in the tree)
# we need to have n (number of satellites left)
# in order to know how many times we need to 
# recurse this function (NO WE DON'T, LEN OF LIST)
# we need the list of non-visited satellites
# and we need the current amount of energy
# we have left we will have two helpers 
# in order to avoid checking the first satellite
# case every time we recurse
def tree_enum_helper_1(sat_list):
    # returns a full tree of all possible paths
    # need to think of a way to traverse the tree
    # in order to find the complete path
    root = sat_tree_node(None)
    
    # first satellites
    for i in range(sat_list):
        new_node = sat_tree_node(sat_list[i])
        new_node.total_energy = new_node.data[0]    # extract energy from satellite
        root.children.update({i: new_node})
        #root.children.update({i: sat_tree_node(sat_list[i])})
        
        # recurse call for branch
        #sats_left = sat_list[:i] + sat_list[i+1:]
        #for j in range(sats_left):
            #new_node = sat_tree_node(sats_left[j])
            #new_
        #root.children[i].children.update({})
    return root
        
        
    # all possible starting satellites are now branches
    
# this one also needs the started tree w/ the root node
# and the first depth of children (all starts)
def tree_enum_helper():
    # returns a completed branch of the tree
    pass
    
                            
if __name__ == "__main__":
    num_sats = int(input())
    # tree structure that has n-1 children
    # root node is a placeholder that has n children
    # each child has n-1 children
    # each child of the children has n-1 children (depricating as we go down)
    
    # children are stored in a dictionary
    # with the key being the satellite name
    # and the value being a list of the children
    
    # the root node is a list of the children
    sat_list = []
    for i in range(num_sats):
        sat_list.append(input().split())
    #root = []
    
    tree = tree_enum_helper_1(sat_list)
    print(tree.children)
    

                            
        
    
    
    
    
    
    
    
    
    
    
    

    # sat_list = []
    # energy = 0

    # traversal_list = []
    # for i in range(num_sats):
    #     sat_list.append(input().split())
    #     path_found = False
    #     first_sat = True
    #     while not path_found:
    #         for j in range(sat_list):
    #             if first_sat:
    #                 pass
    #             if energy >