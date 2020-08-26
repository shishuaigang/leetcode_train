# Merge two sorted linked lists and return it as a new sorted list. The new list
#  should be made by splicing together the nodes of the first two lists.
#
#  Example:
#
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#  Related Topics 链表
#  👍 1234 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 链表需要考虑的几种特殊情况：为空，只有1个节点，只有2个节点
        if not l2:
            return l1
        if not l1:
            return l2
        m = ListNode(None)
        n = m
        while l1 and l2:
            if l1.val <= l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
        if l1:
            n.next = l1
        if l2:
            n.next = l2
        return m.next

# leetcode submit region end(Prohibit modification and deletion)
