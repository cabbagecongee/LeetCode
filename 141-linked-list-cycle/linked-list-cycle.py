# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        visited = [head]
        curr = head
        while curr.next:
            curr = curr.next
            if curr in visited:
                return True
            else:
                visited.append(curr)
        return False