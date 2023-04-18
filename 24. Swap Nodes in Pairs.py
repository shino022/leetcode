# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  """
  1->2->3->4
  1-><-2 3->4 lose the pointer to 3

  p1 p2 p3 p4
  p2 p3 are what we want to swap
  p1.next has to be updated too
  we need p4 to iterate thru

  p4 can be null

  init 
    dummy.next = head # dummy is needed to return head as a result
    p1 = dummy
    p2 = head

  while p2 not null and p2.next not null # we need at least 2 nodes to swap
    # create p3, and p4
    p3 = p2.next
    p4 = p2.next.next # will be needed update p2 later

    # swap
    p1 point to p3
    p3 point to p2 
    p2 point to p4

    # update p1, p2 and p3, p4 will be updated from p2 in the next iteration
    p1 = p2
    p2 = p4

  return dummy.next
  """
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    p1, p2 = dummy, head
    while p1.next and p1.next.next:
      p3 = p2.next
      p4 = p2.next.next

      p1.next = p3
      p3.next = p2
      p2.next = p4
      
      p1 = p2
      p2 = p4
    return dummy.next
