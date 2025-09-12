class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        head_data = head.data
        
        result_head = Node(head_data)         
        previous_result_node = result_head
        
        elements = list()  
        elements.append(head_data)
        
        node = head.next        
        
        while node is not None:  
            node_data = node.data          
            if node_data not in elements:                
                result_node = Node(node_data)              
                previous_result_node.next = result_node
                previous_result_node = result_node
                               
                elements.append(node_data)
                
            node = node.next
        
        return result_head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 