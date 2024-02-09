# Authors: Richard Roy, Justin Birdsall
#
# Author of referenced code: Ajitesh Pathak
# Referenced: 
#   AVL Tree Insertion (and main functionality): https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
#   AVL Tree Deletion: https://www.geeksforgeeks.org/deletion-in-an-avl-tree/


# Below (minus custom func/specified modifications) 
# is from https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
# Author: Ajitesh Pathak
############################################################################################################
# Python code to insert a node in AVL tree 
  
# Generic tree node class 
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree(object): 
############################################################################################################
######## MODIFICATION TO REFERENCED CODE VVV

    # custom init for extractable root
    #def __init__(self):
    #    self.root = None
########        
############################################################################################################
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
############################################################################################################
######## MODIFICATION TO REFERENCED CODE VVV
        
        #prev code vvv
        #if not root: 
            #return TreeNode(key)
            
        #custom code vvv (I didn't like how the root was instantiated in the original code
        #                  so I made it more automatic, with my other change)  
        if not root:
            #self.root = TreeNode(key)
            return TreeNode(key)
########
############################################################################################################
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
############################################################################################################

# Below is from https://www.geeksforgeeks.org/deletion-in-an-avl-tree/
# Author: Ajitesh Pathak
############################################################################################################
    def getMinValueNode(self, root):
            if root is None or root.left is None:
                return root
    
            return self.getMinValueNode(root.left)
    
# Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):
 
        # Step 1 - Perform standard BST delete
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the 
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
############################################################################################################
    
    # custom func to get max value (rightmost node in tree)
    def getMax(self, root):
        # tree is empty
        if not root:
            return None
        # no right subtree (single node or one left child)
        if not root.right:
            return root.val
        else:
            return self.getMax(root.right)
        
        
    


# "Given the inflow and outflow of e-mails and importance of each, can you track the most important e-mail in the stack?"
if __name__ == "__main__":
    num_actions = int(input())
    
    #VVVV strategizing VVVV
    # emails come in a few different formats
    # 1. [1, x] A new e-mail of value x has arrived in his inbox.
        # need to keep a priority stack of emails 
        # add a new email to the stack
        # on this type of input
    # 2. [2] The Goat has dealt with the top e-mail in his stack.
        # the goat keeps a recency stack of emails
        # remove the top email from the recency stack from both the recency and priority stacks
        # on this type of input
    # 3. [3] Print the value of the most important e-mail still in the stack.
        # print the top email from the priority stack
    
    # based on the need to be able to insert and remove values, as well as the need to
    # keep track of max val and next/prev to adjust the max val,
    # an AVL tree is likely the best data structure to use here
    
    

    recency_stack = []
    priority_stack = AVL_Tree()
    root = None
    output = []
    for i in range(num_actions):
        action = input().split()
        # insert new email case
        if int(action[0]) == 1:
           #priority_stack.insert(priority_stack.root, int(action[1]))
           root = priority_stack.insert(root, int(action[1]))
           # reversed because of appends, be aware (pop is LIFO, so it's fine here)
           recency_stack.append(int(action[1]))
        # remove most recent email case
        elif int(action[0]) == 2:
           # convienient, 2 for 1 removal
           #priority_stack.delete(priority_stack.root, int(recency_stack.pop()))
           root = priority_stack.delete(root, int(recency_stack.pop()))
           # testing, print recency stack
           #for i in recency_stack:
           #    print(i)
            # does not properly remove from priority stack
            
        # print max email case
        elif int(action[0]) == 3:
            #print(priority_stack.getMax(priority_stack.root))
            # print on new line
            #print(int(priority_stack.getMax(root)))
            #print(end)
            #print()
            output.append(priority_stack.getMax(root))
    for i in output:
        print(int(i))
        
    
    
    
    
    
    