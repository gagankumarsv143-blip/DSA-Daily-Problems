# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def push(self, x):
        newNode = Node(x)

        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

        self.length += 1

    def pop(self):
        if self.front is None:
            return -1

        x = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.length -= 1
        return x

    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data

    def getSize(self):
        return self.length
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        queue = Queue()
        queue.push(root)
        ans.append([root.val])

        while queue.getSize()>0:
            n = queue.getSize()
            level = []
            for i in range(n):
                front = queue.pop()
                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)

            if len(level)>0:
                ans.append(level)
        return ans
    
       