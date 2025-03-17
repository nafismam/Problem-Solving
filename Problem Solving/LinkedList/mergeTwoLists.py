class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node that acts as a starting point for the new merged list
        dummy = node = ListNode()
        
        # Traverse both lists while neither is empty
        while list1 and list2:
            # Compare the values of the current nodes in both lists
            if list1.val < list2.val:
                # If list1's value is smaller, attach it to the merged list
                node.next = list1
                # Move list1 forward to its next node
                list1 = list1.next
            else:
                # If list2's value is smaller or equal, attach it to the merged list
                node.next = list2
                # Move list2 forward to its next node
                list2 = list2.next
            
            # Move the pointer of the merged list forward
            node = node.next

        # If one of the lists is not empty, attach the remaining elements
        # This works because the lists are already sorted
        node.next = list1 or list2

        # Return the merged list, starting from the first real node (dummy.next)
        return dummy.next
