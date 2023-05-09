# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
  Add them at the index i, if it's over 10 then pass mod of the sum to the next index as a carry
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      res = ListNode() #dummy node to keep the head node
      cur = res
      carry = 0
      while l1 and l2:
        #Create a new node and point to it
        cur.next = ListNode()
        cur = cur.next
        
        #Calculate sum and carry
        summation = l1.val + l2.val + carry
        cur.val = summation % 10
        carry = summation // 10


        #Update pointers
        l1 = l1.next
        l2 = l2.next
      
      #Add rest of nodes in l1
      while l1:
        cur.next = ListNode()
        cur = cur.next

        summation = l1.val + carry
        cur.val = summation % 10
        carry = summation // 10

        l1 = l1.next

      #Add rest of nodes in l2
      while l2:
        cur.next = ListNode()
        cur = cur.next

        summation = l2.val + carry
        cur.val = summation % 10
        carry = summation // 10

        l2 = l2.next
      if carry:
        cur.next = ListNode(carry)
      return res.next
