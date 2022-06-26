class Node:
    #This is Step 2
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    # This is step 1
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        all_nodes = [node.value for node in self]
        if len(all_nodes)==0:
            return "Linked List is empty"
        return "->".join([node.value for node in self])

    def insert_sll(self, location, value):
        if not isinstance(location, int):
            raise ValueError(
                f"Inappropriate type for location: Expecting {type(1)} got {type(location)}"
            )
        if location < -1:
            raise ValueError(
                f"Location should be greater than -2; -1(For Insertion at the end)"
            )

        #Create a new Node
        new_node = Node(value)

        #If The List is Empty
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            if location == 0:
                #If Location is at the begining of the List
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                #If Location is at the end of the List
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                #If Location is in the middle of the List
                prev_node = self.head
                index = 0
                """
                Traverse through the list and identify the 
                two node between which the new node will
                be inserted. call this prev_node and next_node
                """
                while (index < location - 1):
                    prev_node = prev_node.next
                    index += 1
                next_node = prev_node.next

                #Insert at location
                prev_node.next = new_node
                new_node.next = next_node

    def search_sll(self, search_value):
        curr_node = self.head
        index = 0
        while (curr_node is not None):
            if (curr_node.value == search_value):
                return index
            curr_node = curr_node.next
            index += 1
        return -1

    def delete_sll(self, location):
        #If List is Empty
        if self.head == None:
            raise ValueError(f"Cannot delete from an empty Linked List")

        #If only One Element is present
        if self.head == self.tail:
            #If location is first or last
            if (location == 0 or location == -1):
                self.head = None
                self.tail = None
            else:
                raise ValueError(
                    f"Cannot delete element {location}. Only one element present."
                )
        #If more than one element present
        else:
            #If location is last
            if location == -1:
                curr_node = self.head
                while curr_node.next != self.tail:
                    curr_node = curr_node.next
                curr_node.next = None
                self.tail = curr_node
            #If location is in the middle
            elif location == 0:
                first_node = self.head
                self.head = first_node.next
            else:
                curr_node = self.head
                index = 0
                while (index < location):
                    if curr_node == self.tail:
                        raise ValueError(f"Location {location} not found")
                    prev_node = curr_node
                    curr_node = curr_node.next
                    index += 1
                prev_node.next = curr_node.next

    def clear_sll(self):
        if self.head == None:
            raise ValueError(f"Linked List already empty.")
        self.head = None
        self.tail = None

singly_linked_list = SLinkedList()
singly_linked_list.insert_sll(1, '1')
singly_linked_list.insert_sll(-1, '2')
singly_linked_list.insert_sll(-1, '3')
singly_linked_list.insert_sll(-1, '4')
singly_linked_list.insert_sll(-1, '5')
singly_linked_list

singly_linked_list.insert_sll(0, '0')
singly_linked_list.insert_sll(3, '2.5')
singly_linked_list.insert_sll(-1, '6')
singly_linked_list

print(singly_linked_list.search_sll('3'))
print(singly_linked_list.search_sll('30'))

singly_linked_list.delete_sll(3)
singly_linked_list

singly_linked_list.delete_sll(0)
singly_linked_list

singly_linked_list.delete_sll(-1)
singly_linked_list

singly_linked_list.clear_sll()
singly_linked_list

singly_linked_list.clear_sll()
singly_linked_list