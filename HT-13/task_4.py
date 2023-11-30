# 4. Create 'list'-like object, but index starts from 1 and index of 0 raises error. Тобто це
# повинен бути клас, який буде поводити себе так, як list (маючи основні методи), але індексація
# повинна починатись із 1


class ListLike:
    """'List-like Class with main list methods but indexation starts from 1"""

    def __init__(self, *args):
        self.lst = list(args)

    def __getitem__(self, index):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        try:
            return self.lst[index - 1]
        except IndexError:
            raise IndexError("Index out of range")

    def __setitem__(self, index, obj):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        try:
            self.lst[index - 1] = obj
        except IndexError:
            raise IndexError("Index out of range")

    def __len__(self):
        return len(self.lst)

    def __repr__(self):
        return repr(self.lst)

    def append(self, obj):
        """Adds an element at the end of the list"""
        return self.lst.append(obj)

    def clear(self):
        """Removes all the elements from the list"""
        return self.lst.clear()

    def copy(self):
        """Returns a copy of the list"""
        return self.lst.copy()

    def count(self, obj):
        """Returns the number of elements with the specified value"""
        return self.lst.count(obj)

    def extend(self, extention):
        """Add the elements of a list (or any iterable), to the end of the current list"""
        return self.lst.extend(extention)

    def index(self, obj):
        """Returns the index of the first element with the specified value"""
        return self.lst.index(obj) + 1

    def insert(self, index: int, obj):
        """Adds an element at the specified position"""
        return self.lst.insert(index - 1, obj)

    def pop(self, index: int):
        """Removes the element at the specified position"""
        return self.lst.pop(index - 1)

    def remove(self, obj):
        """Removes the item with the specified value"""
        return self.lst.remove(obj)

    def reverse(self):
        """Reverses the order of the list"""
        return self.lst.reverse()

    def sort(self, key: None = None, reverse: bool = False):
        """Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order."""

        return self.lst.sort(key=key, reverse=reverse)


my_list = ListLike(1, 2, 3)
print(my_list[1])

my_list.append(5)
print(my_list)
print(len(my_list))

my_list[4] = 10
print(my_list)

my_list.clear()
print(my_list)

my_list = ListLike(1, 2, 3, 4)
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
