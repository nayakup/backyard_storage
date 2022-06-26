"""
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock 
and we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
"""

from stack import Stack


def stock_span(array):
    result = []
    stack = Stack()
    for index, item in enumerate(array):
        # If STack is empty
        d = {"key": index, "value": item}
        if(stack.is_empty()):
            result.append(-1)
        # If top is greater then item
        elif(stack.peek().get('value') > item):
            result.append(stack.peek().get('key'))
        # if top is less than or equal to item
        elif(stack.peek().get('value') <= item):
            while (stack.peek().get('value') <= item):
                popped = stack.pop()
                if (stack.peek() is None):
                    break
            if(stack.is_empty()):
                result.append(-1)
            else:
                result.append(stack.peek().get('key'))
        stack.push(d)
    return [ind-val for ind, val in enumerate(result)]


input_list = [100, 80, 60, 70, 60, 75, 85]
print(
    f"Result for {input_list} is {stock_span(input_list)}")
