from collections import deque

def BFStree(root):
    if not root:
        return []
    
    result=[]
    q = deque([root])

    while q:
        level=[]
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    
    return result