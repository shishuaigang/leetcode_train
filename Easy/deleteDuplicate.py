# Given a sorted linked list, delete all duplicates such that each element appea
# r only once.
#
#  Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
#  Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
#
#  Related Topics 链表
#  👍 384 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 链表需要考虑只有0个元素或者1个元素的时候
        if not head or not head.next:
            return head
        s = head
        f = head.next
        tmp = ListNode(None)
        tmp.next = s
        while f:
            if s.val == f.val:
                f = f.next
                s.next = f
            else:
                s = f
                f = f.next
        return tmp.next
# leetcode submit region end(Prohibit modification and deletion)