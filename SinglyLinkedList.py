#importing random to generate pseudorandom numbers.
import random

#Class to creates nodes to be added to the queue
class Node:
    #This is the constructor 
    def __init__(self, data): 
        self.data = data
        self.next = None
  
#Class to create a singly linked list
class PriorityQueue: 
    #This is the constructor
    def __init__(self):
        self.head = None

    #Adds node to the start of the queue
    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    #Adds node to the end of the queue
    def append(self, data):
        NewNode = Node(data)
        #If it is the first node
        if self.head is None: 
            self.head = NewNode
            return
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  NewNode 
  
    #Adds node at the correct position in the queue
    def placement(self, data):
        position = self.head
        NewNode = Node(data)
        counter = -1
        while (position):
            if (position.data < int(data)):
                position = self.head
                for i in range(counter):
                    position= position.next
                NewNode.next = position.next
                position.next = NewNode
                return
            else:
                position = position.next
                counter += 1
        PriorityQueue.append(data)
        return

    # Popping Values here    
    def pop(self):
    	temp = self.head.next
    	value = temp.data
    	self.head = temp
    	return value

    #Function to print the elements of the queue
    def Display(self):
        numbers = [] 
        temp = self.head 
        while (temp): 
            numbers.append(temp.data) 
            temp = temp.next
        return numbers

    #Returns the size of the queue
    def Size(self): 
        temp = self.head 
        counter = 0
        while (temp):
            counter += 1  
            temp = temp.next
        return counter
  
#Main function  
if __name__=='__main__': 
    #Creating queue
    PriorityQueue = PriorityQueue()
    values = []
    for x in range(10000):
        num = random.randint(1,100)
        if x == 0:
            PriorityQueue.append("Sentinel")
        else:
            PriorityQueue.placement(num)
    print("Full list is: ")
    print(PriorityQueue.Display())
    for y in range(20):
    	values.append(PriorityQueue.pop())
    print("Popped vales are: ")
    print(values)
    print(PriorityQueue.Size()) 