# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        group_prev = dummy  # node just before the current group

        while True:
            # find the k-th node of this group; if fewer than k remain, stop
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # first node after this group

            # reverse the group; the old first node ends up pointing to group_next
            prev, curr = group_next, group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            old_first = group_prev.next   # becomes the tail of the reversed group
            group_prev.next = kth         # kth is now the head of the group
            group_prev = old_first        # next group starts after this tail