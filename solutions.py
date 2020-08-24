class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        
        for x in nums:
            if x in counter:
                return True
            else:
                counter.add(x)
        
        return False

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize two string vars empty string
        # iterate through both lists
        # initialize two pointers at the value of each listNode
        # iterate through both lists
        # concatenate current values to num strings
        # reverse the strings
        # add them together
        num1 = ""
        num2 = ""
        
        curr1 = l1
        curr2 = l2
        
        while curr1 is not None:
            num1 = num1 + str(curr1.val)
            curr1 = curr1.next
        
        while curr2 is not None:
            num2 = num2 + str(curr2.val)
            curr2 = curr2.next
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        list_vals = str(int(num1) + int(num2))[::-1]
        
        new_list = ListNode(list_vals[0])
        curr = new_list
        
        for x in list_vals[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        
        return new_list
        