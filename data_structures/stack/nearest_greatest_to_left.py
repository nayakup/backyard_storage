from stack import Stack


def get_ngl(array):
    result = []
    stack = Stack()
    for item in array:
        # If STack is empty
        if(stack.is_empty()):
            result.append(-1)
        # If top is greater then item
        elif(stack.peek() > item):
            result.append(stack.peek())
        # if to is less than or equal to item
        elif(stack.peek() <= item):
            while (stack.peek() <= item):
                popped = stack.pop()
                if (stack.peek() is None):
                    break
            if(stack.is_empty()):
                result.append(-1)
            else:
                result.append(stack.peek())
        stack.push(item)
    return result


input_list = [6, 4, 1, 3, 10, 5]
print(
    f"Result for {input_list} is {get_ngl(input_list)}")
