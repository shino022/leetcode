"""
Convert the linked list to an array

Calculate the index of the n-th element from the end of the list
  i = len(l) - n

The element at i will be deleted
if there's an element before i, let it points to l[i].next. doesnt matter if its null
if i is the first element, let head points to l[i].next so i is skipped
return head
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      p = head
      l = []

      # Convert linked list to array
      while p:
        l.append(p)
        p = p.next

      # Calculate the index of the element to be deleted
      i = len(l) - n
      if i > 0:
        # If there is an element before i, let it point to l[i].next       
        l[i-1].next = l[i].next
      else:
        # If i is the first element, let head point to l[i].next
        head = l[i].next
      return head