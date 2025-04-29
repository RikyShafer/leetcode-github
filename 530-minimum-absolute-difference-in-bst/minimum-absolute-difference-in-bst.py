# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)       # קודם כל הולכים שמאלה
            result.append(node.val)  # ואז מוסיפים את הערך של הצומת הנוכחי
            inorder(node.right)      # ואז הולכים ימינה

        inorder(root)
        print(root)

        min_diff = float('inf')  # מתחילים מערך גבוה מאוד
        for i in range(1, len(result)):
            diff = result[i] - result[i - 1]
            min_diff = min(min_diff, diff)

        return min_diff
        