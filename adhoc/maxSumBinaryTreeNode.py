# Python3 program to find maximum path sum in Binary Tree
 
# A Binary Tree Node
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def findMax(root):

    if root is None:
        return 0
 
    # l and r store maximum path sum going through left and right child of root
    l = findMax(root.left)
    r = findMax(root.right)
 
    # Max path for parent call of root
    max_single = max(max(l, r) + root.data, root.data)
 
    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l+r + root.data)
 

    # Store the maximum result
    findMax.res = max(findMax.res, max_top)
 
    return max_single
 

def findMaxSum(root):
 
    # Initialize float
    findMax.res = float("-inf")
 
    # Compute and return result
    findMax(root)
    return findMax.res
 
 
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
 
    # Function call
    print("Max path sum: ", findMaxSum(root))