# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root:
            return []
        self.helper(root, result)
        return result

    def helper(self, root, to_return):
        #go to left child
        if root.left:
            self.helper(root.left, to_return)
        
        to_return.append(root.val)

        if root.right:
            self.helper(root.right, to_return)
        

        