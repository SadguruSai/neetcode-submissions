# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # optimized heap method
        heap=[]

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
            
        dummy=ListNode(0)
        node=dummy
        while heap:
            val,i,temp=heapq.heappop(heap)

            node.next=temp
            node=node.next

            if temp.next:
                heapq.heappush(heap,(temp.next.val,i,temp.next))
        return dummy.next
