class Stack:

    def __init__(self, val_stiva=1, val_stiva2=2):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        self.second = 5
        value = self.__stackList[-1]
        del self.__stackList[-1]
        return value

    def __str__(self):
        return f"{self.__stackList} {self.second}"


obiect_1 = Stack(val_stiva2=1, val_stiva=2)
obiect_2 = Stack()
obiect_1.third = 6
obiect_1.push(3)
obiect_1.pop()
# obiect_2.push(obiect_1.pop())
print(obiect_1.__dict__)
print(obiect_2.__dict__)
# print(obiect_1._Stack__stackList)
# print(obiect_2)


# obiect_1.push(3)
# obiect_1.push(2)
# obiect_1.push(1)
# print(obiect_1.pop())
# print(obiect_1.pop())
# print(obiect_1.pop())
# print(len(obiect_1.stackList))
