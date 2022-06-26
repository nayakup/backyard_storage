from stack import Stack


def get_nsr(array):
    stack = Stack()
    result = []
    array.reverse()
    for item in array:
        # If Stack is empty
        if(stack.is_empty()):
            result.append((-1))
        # If TOP of the Stack is smaller than item
        elif(stack.peek() < item):
            result.append(stack.peek())
        # If TOP of the Stack is large than item
        elif(stack.peek() >= item):
            while(stack.peek() >= item):
                popped = stack.pop()
                if(stack.is_empty()):
                    break
            if(stack.is_empty()):
                result.append((-1))
            else:
                result.append(stack.peek())
        stack.push(item)
    array.reverse()
    result.reverse()
    return result