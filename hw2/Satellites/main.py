# Authors: Richard Roy, Justin Birdsall

class sat_tree_node:
    def __init__(self, data, index):
        self.data = data
        # typecast the data to the correct types
        if self.data is not None:
            self.data[0] = int(self.data[0])    # energy
            self.data[1] = int(self.data[1])    # cost
        self.children = []
        #self.children = {}  # dictionary of children, each is a branch 
                            # with the next satellite being any of the 
                            # satellites in the list that are left
                            # to enumerate all paths
                            # we will need to traverse the tree
                            # and the number of times we traverse the tree
                            # needs to be the number of satellites
                            # so we know we have a valid path
                            
        self.total_energy = 0      # energy
        self.index = index               # index of the satellite in the original list
        
    def traverse(self):
        # traverse the tree
        for i in range(len(self.children)):
            print("Sat info: Index: " + str(tree.children[i].index) + " Data:" + str(tree.children[i].data) + " Total Energy:" + str(tree.children[i].total_energy) + " Children:")# + (for j in range(tree.children[i].children): str(tree.children[i].children[j])))
            if len(self.children[i].children) > 0:
                for j in range(len(self.children[i].children)):
                    print("Child Index: " + str(tree.children[i].children[j].index))
            else:
                print("No children")
            self.children[i].traverse()
            
    def valid_start(self):
        # traverse the tree and find the valid start
        n = len(self.children)
        depth = 0
        
        for start in self.children:
            #if start.valid_start_helper(n, 0) == n:
                #return start.index
                
            if start.valid_start_helper(n-1, depth+1) == n:
                return start.index
        #return -1
        #return self.valid_start_helper(n)
        #depth = self.valid_start_helper(n, 0)
        # decrement i for every traversal
        # go through all paths
        
    def valid_start_helper(self, n, depth):
        # base case
        if n == 0 or len(self.children) == 0:
            return depth
        # recursive case
        else:
            depth_list = []
            for i in range(len(self.children)):
                depth_list.append(self.children[i].valid_start_helper(n-1, depth+1))
            return max(depth_list)
            #for i in range(self.children):
                #return self.children[i].valid_start_helper(n-1, depth+1)
                
                
                            
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
    root = sat_tree_node(None, None)
    
    # first satellites
    #default_sat_dict = {}
    
    # initialize all the satellites into nodes 
    sat_node_list = []
    for i in range(len(sat_list)):
        new_node = sat_tree_node(sat_list[i], i)
        #default_sat_dict.update({i: new_node})
        #default_sat_dict[i].total_energy = default_sat_dict[i].data[0]    # extract energy from satellite
        new_node.total_energy += int(new_node.data[0])
        sat_node_list.append(new_node)
    
    #for i in range(len(sat_list)):
    #root.children = default_sat_dict
    
    # add all the satellites to the root node (all possible starting satellites)
    root.children = sat_node_list
    
    # enumerate all paths
    i = 0
    for sat in root.children:
        # print for error checking
        #print(sat.data[0])
        #print(sat.data[1])
        sat.children = tree_enum_helper(root.children[:i] + root.children[i+1:], sat.total_energy - sat.data[1])    # recurse call for branch (all satellites left) (energy left after this satellite)
        i += 1
        
        
        
        
        
    #for sat in default_sat_dict:
        #root.children.update()
        
        
        #new_node = sat_tree_node(sat_list[i], i)
        #new_node.total_energy = new_node.data[0]    # extract energy from satellite
        #root.children.update({i: new_node})
        #new_node.children = tree_enum_helper(sat_list[:i] + sat_list[i+1:], new_node.total_energy - new_node.data[1])   # recurse call for branch (all satellites left) (energy left after this satellite)
        
        
        
        
        
        
        #root.children.update({i: sat_tree_node(sat_list[i])})
        
        # recurse call for branch
        #sats_left = sat_list[:i] + sat_list[i+1:]
        
        #for j in range(sats_left):
        #    new_node = sat_tree_node(sats_left[j])
        #    new_node
        #root.children[i].children.update({})
    
    return root
        
        
    # all possible starting satellites are now branches
    
# this one also needs the started tree w/ the root node
# and the first depth of children (all starts)
def tree_enum_helper(sat_list, energy):
    # base case
    if len(sat_list) == 0 or energy < 0:    # no more satellites(maybe return 1 instead for this) or no more energy
        return []
    # recursive case
    else:
        # create a list of all the children
        # for the current satellite
        ret_children = []
        i = 0
        for sat in sat_list:
            sat.total_energy = energy + sat.data[0]    # extract energy from satellite
            sat.children = tree_enum_helper(sat_list[:i] + sat_list[i+1:], sat.total_energy - sat.data[1])   # recurse call for branch (all satellites left) (energy left after this satellite)
            ret_children.append(sat)
            i += 1
        return ret_children
    
    
    
    
    
    # returns a completed branch of the tree
    # base case
    #ret_dict = {}
    #if len(sat_list) == 0 or energy < 0:    # no more satellites(maybe return 1 instead for this) or no more energy
    #    return {}
    # recursive case
    #else:
    #    for i in range(len(sat_list)):
    #        new_node = sat_tree_node(sat_list[i])
    #        new_node.total_energy = energy + new_node.data[0]    # extract energy from satellite
    
            
    
                            
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
    #print(tree.children)
    #for i in range(len(tree.children)):
        #print(tree.children[i].data)
        #print child i: data, total_energy, children
        #print("child " + str(tree.children[i].index) + ": Data:" + str(tree.children[i].data) + " Total Energy:" + str(tree.children[i].total_energy) + " Children:" + str(tree.children[i].children))
        
        #print(tree.children[i].total_energy)
        #print(tree.children[i].children)
    #tree.traverse()
    print(tree.valid_start())

                            
        
    
    
    
    
    
    
    
    
    
    
    

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