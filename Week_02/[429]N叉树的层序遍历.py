# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其层序遍历: 
# 
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#  
# 
#  
# 
#  说明: 
# 
#  
#  树的深度不会超过 1000。 
#  树的节点总数不会超过 5000。 
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            if len(res) <= depth:
                res.append([])
            res[depth].append(root.val)
            for ch in root.children:
                dfs(ch, depth+1)
        dfs(root, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
