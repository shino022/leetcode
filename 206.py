"""
let c to point to p but we need an extra pointer to keep c.next
initialize p with null and c with head node
so in the first iteration c is going to point to null
and from the second c is goint to point to prev node

N:null
@:node
->:next

1. store t
  p  c  t
  N  @->@->@->@...
2. let c points to p
  p  c  t
  N<-@  @->@->@...
3. shift p to c and c to t
  p  c  t
  N<-@  @->@->@...
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      current = head
      prev = None
      while current :
        temp = current.next
        current.next = prev
        prev = current
        current = temp
      head = prev
      return head