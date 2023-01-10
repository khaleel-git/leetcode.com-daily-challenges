# Build_Tree is my self-made library which generates a binary tree
import Build_Tree 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
       # the idea is that traverse each tree, if it traversed at the same heirarchy 
       # then both trees are identical, if not both trees are not identical
       if(p==None and q==None): return True
       if(p==None or q==None): return False

       return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


if __name__ == "__main__":
    p = [1, 2, 3, None, None, 4, 5, 6, 8, 9, 10, 11, 12]
    q = [1, 2, 3, None, None, 4, 5, 6, 8, 9, 10, 11, 12]
    root_p = Build_Tree.build_tree(p)
    root_q = Build_Tree.build_tree(q)

    s = Solution()
    bool_status = s.isSameTree(root_p,root_q)
    if(bool_status == True):
        print(f"Both Trees are identical")
    else:
        print(f"Both Trees are not identical")