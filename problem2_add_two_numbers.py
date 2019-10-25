# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        should_add_one = 0
        result = ListNode(0)
        result_tail = result

        while l1 or l2 or should_add_one:
            value1 = (l1.val if l1.val else 0)
            value2 = (l2.val if l2.val else 0)
        
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
                

            outVal = value1 + value2 + should_add_one
            should_add_one = 0

            if outVal > 10 or outVal == 10:
                should_add_one = 1
                outVal = outVal%10
            


            '''
            each time, result_tail will be a single linked list 
            after the following operations, but the result_tail 
            will keep connecting the next elements.
            '''
            result_tail.next = ListNode(outVal)
            #print ("what now")
            #print (result_tail)
            result_tail = result_tail.next
            #print ("after")
            
            #print (result_tail)
            #print (result)
             
            

        #print ("final")
        #print (result)
        '''
        after operating all the result_tail linked list, 
        we jump the first element of result, which is 0.
        Then the following items will be in correct order
        from the contribution of result_tail
        '''
        return result.next
        

