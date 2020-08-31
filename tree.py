from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树遍历迭代法(递归法比较简单，此处省略)
# 1、先序遍历
def pre_order_traversal(root: TreeNode):
    ret = []
    if not root:
        return ret
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            ret.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
    return ret


# 2、中序遍历
def in_order_traversal(root: TreeNode):
    ret = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        ret.append(cur.val)
        cur = cur.right
    return ret


# 3、后序遍历
# 后序遍历相当于先序遍历左右子树颠倒过来，然后输出结果逆序，因为先序遍历是"中-左-右"，左右子树颠倒过来，就是"中-右-左"，然后在逆序就是"左-右-中"
def post_order_traversal(root: TreeNode):
    if not root:
        return []
    ret = []
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            ret.append(cur.val)
            stack.append(cur.left)
            stack.append(cur.right)
    return ret[::-1]


# 4、层序遍历
def level_order_traversal(root: TreeNode):
    ret = []
    if not root:
        return ret
    q = deque([root])
    while len(q):
        l = []
        for i in range(len(q)):
            node = q.popleft()
            l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ret.append(l)
    return ret


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
