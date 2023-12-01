# 4. Create 'list'-like object, but index starts from 1 and index of 0 raises error. Тобто це
# повинен бути клас, який буде поводити себе так, як list (маючи основні методи), але індексація
# повинна починатись із 1


class ListLike(list):
    """List-like Class with main list methods but indexation starts from 1"""

    def __init__(self, iterable):
        super().__init__(item for item in iterable)

    def __setitem__(self, index, item):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        try:
            super().__setitem__(index - 1, item)
        except IndexError:
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        try:
            return super().__getitem__(index - 1)
        except IndexError:
            raise IndexError("Index out of range")

    def index(self, obj):
        """Returns the index of the first element with the specified value"""
        return super().index(obj) + 1

    def insert(self, index: int, obj):
        """Adds an element at the specified position"""
        return super().insert(index - 1, obj)

    def pop(self, index: int):
        """Removes the element at the specified position"""
        return super().pop(index - 1)


my_list = ListLike([1, 2, 3])
print(my_list[1])

my_list.append(5)
print(my_list)
print(len(my_list))

my_list[4] = 10
print(my_list)

my_list.clear()
print(my_list)

my_list = ListLike([1, 2, 3, 4])
print(my_list.index(2))

my_list.insert(3, "k")
print(my_list)

print(my_list.pop(3))
print(my_list)

my_list.remove(4)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# print(my_list[0])
# print(my_list[4])
# my_list[0] = 8
# my_list[7] = 8
