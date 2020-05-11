#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      if root == None:
        return []
      parentArr = [] #3
      levelCounter = 0

      parentArr.append([root.val])
      self.levelOrderHelper(root, 1, parentArr)
      
      return parentArr
    def levelOrderHelper(self, root, levelCounter, parentArr):

      if root.left != None:
        if len(parentArr) >= levelCounter + 1:
           parentArr[levelCounter].append(root.left.val)
        else:
           parentArr.append([root.left.val])

        self.levelOrderHelper(root.left, levelCounter + 1, parentArr)  

      if root.right != None:
        if len(parentArr) >= levelCounter + 1:
           parentArr[levelCounter].append(root.right.val)
        else:
           parentArr.append([root.right.val])
        #print("root right value is: {} levelCounter is {}".format(root.right.val, levelCounter))
        self.levelOrderHelper(root.right, levelCounter + 1, parentArr)  

