class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        print(f"{self.args} снесен, но он останется в истории")





    # def __init__(self, name, number_of_floors):
    #     self.name = name
    #     self.number_of_floors = number_of_floors


    # def __eq__(self, other):
    #     if isinstance(other, int):
    #         return self.number_of_floors == other
    #     else:
    #         return self.number_of_floors == other
    #
    # def __lt__(self, other):
    #     if isinstance(other, int):
    #         return self.number_of_floors < other
    #     else:
    #         return self.number_of_floors < other
    #
    # def __le__(self , other):
    #     if isinstance(other, int):
    #         return self.number_of_floors <= other
    #     else:
    #         return self.number_of_floors <= other
    # def __gt__(self , other):
    #     if isinstance(other, int):
    #         return self.number_of_floors > other
    #     else:
    #         return self.number_of_floors > other
    # def __ge__(self , other):
    #     if isinstance(other, int):
    #         return self.number_of_floors >= other
    #     else:
    #         return self.number_of_floors >= other
    # def __ne__(self, other):
    #     if isinstance(other, int):
    #         return self.number_of_floors != other
    #     else:
    #         exit()
    # def __add__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floors += value
    #         return self
    # def __iadd__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floors += value
    #         return self
    # def __radd__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floors += value
    #         return self
    #
    # def __str__(self):
    #     return f'Название: {self.name} кол-во этажей:{self.number_of_floors}'




h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__