# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # start = head
        # end = head
        # length = 1
        # while end.next:
        #     end = end.next
        #     length += 1
        
        # i = length
        # while i > (length - n):
        #     start = start.next
        #     i -= 1
        # if not start:
        #     return ListNode()
        # if start.next and start.next.next:
        #     start.next = start.next.next
        # elif start.next:
        #     start.next = None 
        # elif not head.next and n == 1:
        #     return ListNode()

        # return head
        
        start = head
        end = head
        for i in range(n):
            if end.next:
                end = end.next
            else:
                return head.next
        
        while end.next:
            start = start.next
            end = end.next
        
        if not start or start == end:
            return None
        elif start.next and not start.next.next:
            start.next = None
        elif start.next.next:
            start.next = start.next.next
        return head