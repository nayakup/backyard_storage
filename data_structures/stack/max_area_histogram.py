from stack import Stack

def get_nsr(array):
    stack = Stack()
    result = []
    array.reverse()
    for index, item in enumerate(array):
        # If Stack is empty
        d = {"key": index, "value": item}
        if(stack.is_empty()):
            result.append((-1))
        # If TOP of the Stack is smaller than item
        elif(stack.peek().get('value')  < item):
            result.append(stack.peek().get('key'))
        # If TOP of the Stack is large than item
        elif(stack.peek().get('value')  >= item):
            while(stack.peek().get('value')  >= item):
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


def get_nsl(array):
    stack = Stack()
    result = []
    for index, item in enumerate(array):
        # If Stack is empty
        d = {"key": index, "value": item}
        if(stack.is_empty()):
            result.append((-1))
        # If TOP of the Stack is smaller than item
        elif(stack.peek().get('value') < item):
            result.append(stack.peek().get('key'))
        # If TOP of the Stack is large than item
        elif(stack.peek().get('value') >= item):
            while(stack.peek().get('value') >= item):
                popped = stack.pop()
                if(stack.is_empty()):
                    break
            if(stack.is_empty()):
                result.append((-1))
            else:
                result.append(stack.peek().get('key'))
        stack.push(d)
    return result


def max_area_histogram(array):
    nsr = get_nsr(array)
    return nsr
    nsl = get_nsl(array)
    return nsl


arr = [6, 2, 5, 4, 5, 1, 6]
max_area = max_area_histogram(arr)

print(arr)
print(max_area)