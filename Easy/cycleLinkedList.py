# Given a linked list, determine if it has a cycle in it.
#
#  To represent a cycle in the given linked list, we use an integer pos which re
# presents the position (0-indexed) in the linked list where tail connects to. If
# pos is -1, then there is no cycle in the linked list.
#
#
#
#
#  Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the s
# econd node.
#
#
#
#
#
#
#  Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the f
# irst node.
#
#
#
#
#
#
#  Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
#
#  Follow up:
#
#  Can you solve it using O(1) (i.e. constant) memory?
#  Related Topics 链表 双指针
#  👍 729 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 链表如果有环，那么节点肯定再次会出现
        tmp = {}
        while head:
            if not tmp.get(head):
                tmp[head] = 1
                head = head.next
            else:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)