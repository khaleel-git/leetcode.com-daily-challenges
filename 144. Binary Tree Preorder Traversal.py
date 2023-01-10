from collections import deque

def build_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(lst):
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            if lst[i+1] is not None:
                node.right = TreeNode(lst[i+1])
                queue.append(node.right)
        i += 2
    return root

def print_tree(root):
    if not root:
        return
    
    print(root.val, end=": ")
    if(root.left !=None):
        print("left_node=", root.left.val, end=" ")
    if(root.right !=None):
        print("right_node", root.right.val, end=" ")
    print("") # for new line

    # Recursion call
    print_tree(root.left)
    print_tree(root.right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []   
        result = [root.val]
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result

if __name__ == "__main__": 
    # Build the tree
    lst = [1, 2, 3, None, None, 4, 5, 6, 8, 9, 10, 11, 12]
    # Print the tree
    root = build_tree(lst)
    
    print_tree(root)

    # Create an object of the Solution class
    solver = Solution()

    # Call the preorderTraversal method on the object and pass in the root node of the tree as an argument
    result = solver.preorderTraversal(root)

    # Print the result
    print(result)