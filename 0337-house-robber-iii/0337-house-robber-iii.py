# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return [0, 0]
            
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)
            
            with_node = node.val + left_pair[1] + right_pair[1]
            without_node = max(left_pair) + max(right_pair)
            
            return [with_node, without_node]
        
        return max(dfs(root))
        