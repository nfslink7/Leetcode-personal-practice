"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        # initialize the queue with root node (for level order traversal)
        queue = collections.deque([root])

        # start the traversal
        while queue:
            size = len(queue)  # get number of nodes on the current level
            for i in range(size):
                node = queue.popleft()  # pop the node

                # An important check so that we do not wire the node to the node on the next level.
                if i < size - 1:
                    node.next = queue[0]  # because the right node of the popped node would be the next in the queue.

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root