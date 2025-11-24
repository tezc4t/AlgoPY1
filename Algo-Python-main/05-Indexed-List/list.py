class IndexedList:
    def __init__(self, value):
        self.data = [value]
        self.length = 1

    def print_list(self):
        for value in self.data:
            print(value)

    def append(self, value):
        pass

    def pop(self):
        pass

    def prepend(self, value):
        pass

    def pop_first(self):
        pass

    def get(self, index):
        pass

    def set_value(self, index, value):
        pass

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass


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
