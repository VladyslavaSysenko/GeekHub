# 3. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.


class MyClass:
    _ids = 0

    def __init__(self):
        MyClass._ids += 1
        self.id = MyClass._ids

    @property
    def ids(self):
        return self._ids


a = MyClass()
print(a.ids)
b = MyClass()
print(b.ids)
c = MyClass()
print(c.ids)
