class IndexedList:
    def __init__(self, value):
        self.data = [value]
        self.length = 1

    def print_list(self):
        for value in self.data:
            print(value)

    def append(self, value):
        self.data.append(value)
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        removed = self.data.pop()
        self.length -= 1
        return removed

    def prepend(self, value):
        self.data.insert(0, value)
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        removed = self.data.pop(0)
        self.length -= 1
        return removed

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        return self.data[index]

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        self.data[index] = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        self.data.insert(index, value)
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        removed = self.data.pop(index)
        self.length -= 1
        return removed


# ------------------------------
# EXAMPLE
# ------------------------------

my_list = IndexedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print("IndexedList before operations:")
my_list.print_list()

my_list.remove(1)
my_list.insert(1, 99)
my_list.set_value(0, 42)

print("\nIndexedList after operations:")
my_list.print_list()
