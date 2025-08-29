"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldTocopy={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            OldTocopy[cur]=copy 
            cur=cur.next
        cur=head
        while cur:
             copy=OldTocopy[cur]
             copy.next=OldTocopy[cur.next]
             copy.random=OldTocopy[cur.random]
             cur=cur.next
        return OldTocopy[head]




    