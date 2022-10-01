# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow =  head
        fast  = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow


'''
If anyone, like me, was still having trouble understanding, the following helped me figure it out. It helped me understand linked lists in general (by viewing each element of the list as a memory index).
■▬▬▬▬▬▬▬▬▬▬■
When progressing through a linked list, think of "head" as indicating the start of that list and therefore the "memory index" that starts the list. You cannot change head directly, by say doing head.next, as that first value is now "removed" (technically a linked list item cannot be deleted, only have its references removed which effectively deletes it). In a linked list, each value (aside from head) contains two memory indexes: its own and the memory index of the next value.

So, when assigning "slow" or "fast" (as an example) to head (slow, fast = head, head) you are simply assigning those two variables to that memory index which lets you traverse the list without messing with the head value (again, head is simply the first value of the list and points to that memory index; its not the list itself per-se). Now you can proceed to traverse the list using your two variables; in this case slow and fast. IMPORTANT TO KEEP IN MIND, by updating these variables you are simply modifying where the list begins so if in a [1, 2 ,3 4] example fast.next would make fast = [2, 3, 4]. This is why you don't modify head itself unless you wish to delete the first variable.

For example, if you want to remove the middle variable, once you get through your while loop to the end of fast, slow should now be at the value (again, think of these as pointing to a memory index slot) in the middle. Unlike a regular list which, should you wish to add/remove a new variable (using say insert), would need to shift everything over one at a time (not good for large data sets), a linked list would only require you to update what your current variable points to. So if our linked list is [1, 2, 3, 4, 5], when fast reached the end slow would be at 2. To remove 3 ( the center ), we would do slow.next = slow.next.next (because the current position of the slow variable is at that memory index of 3 and because that 3 variable holds the information of which memory index value to point to next and 4 doesn't carry information about it's previous value, as its not a doubly linked list, we'd overwrite the memory index value at 3 to now equal the UNIQUE memory index of 4. Making our list now [1, 2, 4, 5]

Once you know how linked lists work, everything else begins to fall into place.

So why can you return head if you modify the list using fast or slow? Because it's all the same list you're modifying (think of the unique memory indexes), you're not creating a separate list by assigning fast or slow to the head; just setting them to that memory index in that chain then proceeding the navigate that same chain and making changes.
■▬▬▬▬▬▬▬▬▬▬■
If you just wanted to return the second half of the list, use fast and slow again with fast progressing as fast.next.next while slow at slow.next the once fast reaches the end, slow will be at the second half of the list. In the above example, that would be [3, 4, 5]
■▬▬▬▬▬▬▬▬▬▬■
Not the best explanation, but linked lists took me longer than I'd like to admit to figure out even with all the resources out there so I hope my "epiphany" helps anyone else struggling.
'''