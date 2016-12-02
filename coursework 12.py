""" Implement TREE_SORT algorithm in a language of your choice, but make sure that the INORDER function is implemented iteratively. """
class BinTreeNode(object):
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None 
       
def tree_insert(tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
            
def in_order_iter(tree):
    """ iteratively sort through a tree """
    stack = []
    done = False
    
    while not done:
        if tree is not None:
            """ start at the top of the tree go left till end. when there are no more left entries, take the next right, back track up if there are no more entries, then go again"""
            stack.append(tree)
            tree = tree.left
        else:
            if (len(stack) > 0):
                """ print out the value """
                tree = stack.pop()
                print(tree.value)
                """ switch to right sub tree """
                tree = tree.right
            else:
                done = True
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def sort(alist):
    """ populate tree from list using first item as start value"""
    start = alist.pop(0)
    t = tree_insert(None, start)
    for i in alist:
        tree_insert(t, i)
    in_order(t)
    in_order_iter(t)
