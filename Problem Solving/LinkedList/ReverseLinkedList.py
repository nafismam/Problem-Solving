# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        before = None
        temp = head #tail head rki 
        after = temp.next

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp  = after
        
        return before

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         prev, curr = None, head
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev, curr = curr, temp
#         return prev
        

        #solution with 0ms run time mine was 3ms

