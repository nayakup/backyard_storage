from stack import Stack


def get_ngr(array):
    result = []
    result_item_stack = Stack()
    array.reverse()
    for item in array:
        # If Stack is empty push -1 in result and item in stack
        if result_item_stack.is_empty():
            result_item_stack.push(item)
            result.append(-1)
            continue
        # if item is greater than top, keep popping the top till item is less than top
        while(item > result_item_stack.peek()):
            popped_item = result_item_stack.pop()
            if(result_item_stack.peek() is None):
                break
        
        if(result_item_stack.peek() is None):
                break
        if item < result_item_stack.peek():  # if item is less than top, push top to result and item to stack
            result.append(result_item_stack.peek())
            result_item_stack.push(item)

    result.reverse()
    return result


input_list = [1, 3, 2, 5, 7]
print(
    f"Result for {input_list} is {get_ngr(input_list)}")

# input_list = [10, 1, 3, 7, 4, 6, 2, 8]
# print(
#     f"Result for {input_list} is {get_ngr(input_list)}")
 