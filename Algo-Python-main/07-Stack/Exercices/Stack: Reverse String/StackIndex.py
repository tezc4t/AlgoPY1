class StackArray:
    def __init__(self, value=None):
        self.stack = []
        if value is not None:
            self.stack.append(value)

    def print_stack(self):
        # On affiche du haut vers le bas (top = fin du tableau)
        for value in reversed(self.stack):
            print(value)

    def push(self, value):
        self.stack.append(value)
        return True

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def height(self):
        return len(self.stack)

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return True if len(self.stack) == 0 else False



if __name__ == "__main__":
    my_stack = StackArray(4)
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)

    print('Stack before pop():')
    my_stack.print_stack()

    print('\nPopped value:')
    print(my_stack.pop())

    print('\nStack after pop():')
    my_stack.print_stack()
