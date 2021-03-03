from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
二叉树遍历迭代法(递归法比较简单，此处省略)
以下是先序、中序、后序遍历到迭代法都是自己写的，没有参考别人到精妙解法，因为别人的精妙代码是别人想出来的，自己记不住
这三种遍历方法套路都是一样的，正所谓一招鲜吃遍天下，这样下次还能写出来，不容易忘记
"""


# 1、先序遍历
def pre_order_traversal(root: TreeNode):
    ans = []
    if not root:
        return ans
    stack = [root]
    while stack:
        node = stack.pop()
        ans.append(node.val)
        # 先向stack中加入right，后加入left
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans


# 2、中序遍历
def in_order_traversal(root: TreeNode):
    ans = []
    if not root:
        return ans
    # stack中放入节点顺序依次是：右节点、中节点、左节点
    stack = [root]
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            ans.append(node.val)
        else:
            if node.right:
                stack.append(node.right)
                # 要将node的右节点设置为None，不然下次遍历又把右节点加入到stack中了
                node.right = None
            # 先将右节点放入stack中，再放入根节点
            stack.append(node)
            if node.left:
                stack.append(node.left)
                node.left = None
    return ans


# 3、后序遍历
def post_order_traversal(root: TreeNode):
    ans = []
    if not root:
        return ans
    # stack中放入节点顺序依次是：根节点、右节点、左节点
    stack = [root]
    while stack:
        # 根节点不弹出来，再放入右节点
        node = stack[-1]
        if not node.left and not node.right:
            stack.pop()
            ans.append(node.val)
        else:
            if node.right:
                stack.append(node.right)
                # 要将node的右节点设置为None，不然下次遍历又把右节点加入到stack中了
                node.right = None
            if node.left:
                stack.append(node.left)
                # 要将node的左节点设置为None，不然下次遍历又把左节点加入到stack中了
                node.left = None
    return ans


# 4、层序遍历BFS
def level_order_traversal(root: TreeNode):
    ans = []
    if not root:
        return ans
    q = deque([root])
    while len(q) > 0:
        level_list = []
        for i in range(len(q)):
            node = q.popleft()
            level_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level_list)

    return ans


# 4、层序遍历DFS
class Solution:
    def levelOrder(self, root: TreeNode):
        ans = []
        self.dfs(root, ans , 0)
        return ans

    def dfs(self, root, ans, level):
        if not root:
            return
        if len(ans) < level + 1:
            ans.append([root.val])
        else:
            ans[level].append(root.val)
        self.dfs(root.left, ans, level + 1)
        self.dfs(root.right, ans, level + 1)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    assert pre_order_traversal(node1) == [1, 2, 3]

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node2.left = node3
    assert pre_order_traversal(node1) == [1, 2, 3]

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5
    node3.right = node6
    assert pre_order_traversal(node1) == [1, 2, 4, 3, 5, 6]

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    assert post_order_traversal(node1) == [3, 2, 1]

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node2.left = node3
    assert post_order_traversal(node1) == [3, 2, 1]

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5
    node3.right = node6
    assert post_order_traversal(node1) == [4, 2, 5, 6, 3, 1]
