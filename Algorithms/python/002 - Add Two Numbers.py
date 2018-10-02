class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(0)
        head = curr
        p, q = l1, l2
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y
            carry = sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p is not None: p = p.next
            if q is not None: q = q.next

        if carry > 0:
            curr.next = ListNode(carry)

        return head.next