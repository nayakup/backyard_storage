class Node:
    # This is Step 2
    def __init__(self, value):
        self.value = value
        self.next = None


class CLinkedList:
    # This is step 1
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

    def __repr__(self):
        all_nodes = [node.value for node in self]
        if len(all_nodes) == 0:
            return "Linked List is empty"
        return "->".join(all_nodes)+f" |({self.tail.value}=>{self.tail.next.value})"

    def insert_cll(self, location, value):
        # Create a new Node
        new_node = Node(value)

        # If The List is Empty
        if (self.head is None):
            if location != 0:
                raise ValueError(
                    "Specify location as zero since Linked List is empty")
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            #Insert at First Location
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            #Insert at Last Location
            if location == -1:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node
            #Insert at Any Location
            else:
                curr_node = self.head
                index = 0
                while (index < location - 1):
                    curr_node = curr_node.next
                    index += 1
                    #If reached the end of list without finding the location
                    if(curr_node.next==self.head):
                        break
                if(curr_node.next==self.head):
                    #If reached the end of list without finding the location, insert at the end
                    new_node.next = self.head
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    #Insert at the location
                    next_node = curr_node.next
                    curr_node.next = new_node
                    new_node.next = next_node


c_linked_list = CLinkedList()
c_linked_list.insert_cll(0, '1')
c_linked_list.insert_cll(0, '0')
c_linked_list.insert_cll(0, '-1')
c_linked_list.insert_cll(-1, '2')
c_linked_list.insert_cll(-1, '3')
c_linked_list.insert_cll(-1, '5')
c_linked_list.insert_cll(-1, '6')
c_linked_list.insert_cll(-1, '7')
c_linked_list.insert_cll(5, '4')

print(c_linked_list)


c_linked_list = CLinkedList()
c_linked_list.insert_cll(0, '1')
c_linked_list.insert_cll(-1, '3')
c_linked_list.insert_cll(-1, '5')
c_linked_list.insert_cll(-1, '7')
c_linked_list

c_linked_list.insert_cll(4, '9')
c_linked_list