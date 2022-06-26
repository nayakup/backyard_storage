class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items == []:
            return self.items.pop()
        return None
        
    def peek(self):
        if not self.items == []:
            return self.items[-1]
        return None

    def contains(self, value):
        return value in self.items

    def is_empty(self):
        return self.items == []

    def __repr__(self):
        return '\n'.join([str(x) for x in self.items[::-1]])

    def __iter__(self):
        for item in self.items:
            yield item


# stack = Stack()
# stack.push('A')
# stack.push('B')
# stack.push('C')
# stack.push('D')
# stack.push('E')
# print(stack)
# print('----Run Pop-----')
# stack.pop()
# print(stack)
# print('----Run Peek-----')
# print(stack.peek())
# print(stack)
# print('----Run Contains-----')
# print(stack.contains('C'))
# print(stack.contains('G'))
# print(stack)
# print('----Pop All elements-----')
# print((stack.pop()))
# print((stack.pop()))
# print((stack.pop()))
# print((stack.pop()))
# print(stack)
# print('----Pop empty stack-----')
# print((stack.pop()))
