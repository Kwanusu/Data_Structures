class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        node = Node(data)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("No values")
            return
        current = self.head
        values = ""
        while current:
            values += str(current.data) + "-->"
            current = current.next
        print(values)
        
    def insert_at_end(self, data):
        node  = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        current_index = 0

        while current is not None and current_index < index - 1:
            current = current.next
            current_index += 1

        current.next = current.next.next
        
    def insert_at(self, index, data):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head
        current_index = 0

        while current is not None and current_index < index - 1:
            current = current.next
            current_index += 1
        node.next = current.next
        current.next = node
        
    def insert_after_value(self, data_after, data_to_insert):
        current = self.head
   
        while current is not None:
            if current.data == data_after:
           
                new_node = Node(data_to_insert)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            
    def remove_after_value(self, data_after):
        current = self.head

        while current is not None:
            if current.data == data_after:
                if current.next is not None:  
                    current.next = current.next.next
                return  
            current = current.next
   
        
            
            
ll = LinkedList()
ll.insert_at(0, 301)
ll.insert_at(1, 492)
ll.insert_at(2, 343)
ll.insert_at(3, 524)
ll.insert_at(4, 735)

print("Initial list:")
ll.print()

# Testing insert_at
ll.insert_at(2, 643)
print("\nAfter inserting 643 at index 2:")
ll.print()

# Testing remove_at
ll.remove_at(4)
print("\nAfter removing element at index 4:")
ll.print()

# Testing insert_after_value
ll.insert_after_value(343, 578)
print("\nAfter inserting 578 after value 343:")
ll.print()

# Testing remove_after_value
ll.remove_after_value(343)
print("\nAfter removing the element after value 343:")
ll.print()            