
# // https://leetcode.com/problems/maximum-depth-of-binary-tree/

# // The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# //   Note: A leaf is a node with no children.

# //     Example:

# // Given binary tree[3, 9, 20, null, null, 15, 7],

# //    3
# //   / \
# //  9   20
# //     /  \
# //    15   7
#             \
#              69
# // return its depth = 3.


# /**
#  * Definition for a binary tree node.
#  * function TreeNode(val) {
#  *     this.val = val;
#  *     this.left = this.right = null;
#  * }
#  */
# /**
#  * @param {TreeNode} root
#  * @return {number}
#  */
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None



def maxDepth(root: TreeNode) -> int:
    if root is None:
      return -1
    return maxDepthHelper(root)


def maxDepthHelper(node, depthCounter = 1):
    if node.left == None and node.right == None:
      return depthCounter

    maxLeft = 0
    maxRight = 0
    if node.left != None:
      maxLeft = maxDepthHelper(node.left, depthCounter+1)

    if node.right != None:
      maxRight = maxDepthHelper(node.right, depthCounter+1)



    return maxLeft if maxLeft > maxRight else maxRight
    # return max(maxLeft,maxRight)


    public int maxDepth(TreeNode root) {
        return root==null? 0 : Math.max(maxDepth(root.left), maxDepth(root.right))+1;
    }

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
t.right.right.right = TreeNode(69)

print(maxDepth(t))

    
