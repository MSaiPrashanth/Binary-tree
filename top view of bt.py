class Node:
    def __init__(self,d):
        self.lc=None
        self.rc=None
        self.d=d
        self.hd=0
def topview(root):
    m={}
    q=[]
    q.append(root)
    while len(q)>0:
        node=q.pop(0)
        if node.hd not in m:
            m[node.hd]=node.d
        if node.lc:
            node.lc.hd=node.hd-1
            q.append(node.lc)
        if node.rc:
            node.rc.hd=node.hd+1
            q.append(node.rc)
    print("Top view ")
    for k in sorted(m):
        print(m[k],end=",")        
root=Node(1)
root.lc=Node(2)
root.rc=Node(3)
root.lc.lc=Node(4)
root.lc.rc=Node(5)
root.lc.lc.rc=Node(7)
root.lc.lc.rc.lc=Node(9)
root.lc.lc.rc.lc.lc=Node(10)
root.rc.rc=Node(6)
root.rc.rc.lc=Node(8)
root.rc.rc.lc.rc=Node(11)
topview(root)