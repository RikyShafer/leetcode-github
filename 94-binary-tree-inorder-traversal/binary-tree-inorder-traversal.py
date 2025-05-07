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
        sol=[]

        def er(root):

            if root is None:
                return sol
            if root.left:
                er(root.left) 
            sol.append(root.val)    
            if root.right:
                er(root.right) 
        er(root)        
        return sol
        





# מה שאני חושבת לעשות זה בעצם רוקרסיה ששולחת בעצם קודם את צד שומאת ואז את צד ימין 
#בעצם מה שהיה לי הוא יסרוק את צד ימים ואז אחרי שיגמר יסויך את האבא ואז ילך  לתת עת הימיני     




        
        