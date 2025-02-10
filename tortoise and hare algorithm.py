def hasCycle(self, head):
    #Handle Empty List or Single Node
    if not head or not head.next:
        return False
    

    # Initialize slow and fast pointer
    slow = head
    fast = head.next 

    # move pointer until they meet or fast reaches
    while slow != fast:
        # if fast pointer reaches end, or no cycle exits
        if not fast or not fast.next:
            return False
        
        # Move slow one step and fast two steps

        slow = slow.next
        fast = fast.next.next 


    # if we exit the loop, pointers have met 
    return True 