
class Train:
    def __init__(self,item_name,appointments,train_number,departure_time):
        self.item_name = item_name
        self.appointments = appointments
        self.train_number = train_number
        self.departure_time = departure_time


tata = Train("кирова","Новосибирск",12,23)
a = input("введите куда идет поезд: ")
if a == tata.appointments:
    print(tata.item_name, tata.appointments, tata.train_number, tata.departure_time)


class Two:
    def __init__(self, two1, one):
        self.one = one
        self.two1 = two1

    def vivod_ikpan(self):
        print(self.one)
        print(self.two1)

    def ucmemia(self, new_one, new_two1):
        self.one = new_one
        self.two1 = new_two1

    def simma(self):
        c = self.two1 + self.one
        print(c)

    def vod(self):
        if self.two1 > self.one:
            print(self.two1)
        else:
            print(self.one)


a = Two(20, 30)
print("Исходные значения:")
a.vivod_ikpan()
print("\nВычисление суммы:")
a.simma()
print("\nНахождение наибольшего значения:")
a.vod()
print("\nИзменение значений:")
a.ucmemia(50, 10)
print("\nЗначения после изменения:")
a.vivod_ikpan()
print("\nВычисление суммы после изменения:")
a.simma()
print("\nНахождение наибольшего значения после изменения:")
a.vod()

class Counter():
    def __init__(self, counter=0):
        self.counter = counter

    def plus(self):
        self.counter += 1

    def minus(self):
        self.counter -= 1

    def now(self):
         return self.counter

counter1 = Counter()
print("Counter1 (по умолчанию):", counter1.now())

counter2 = Counter(5)
print("Counter2 (начальное значение 5):", counter2.now())

counter2.plus()
print("Counter2 после увеличения:", counter2.now())

counter2.minus()
print("Counter2 после уменьшения:", counter2.now())

current_value = counter2.now()
print("Текущее значение Counter2 (получено через свойство):", current_value)


class MyClass:

    def __init__(self, property1=0, property2="default"):

        self.property1 = property1
        self.property2 = property2
        print(f"Объект MyClass создан со свойствами: {self.property1}, {self.property2}")

    def __del__(self):

        print(f"Объект MyClass со свойствами {self.property1}, {self.property2} удален.")

    def display_properties(self):

        print(f"Свойство 1: {self.property1}")
        print(f"Свойство 2: {self.property2}")



print("Демонстрация возможностей класса MyClass:")


print("\nСоздание объекта с конструктором по умолчанию:")
obj1 = MyClass()
obj1.display_properties()

print("\nСоздание объекта с конструктором с параметрами:")
obj2 = MyClass(10, "Hello")
obj2.display_properties()


print("\nИзменение свойств объекта:")
obj2.property1 = 20
obj2.property2 = "World"
obj2.display_properties()


print("\nУдаление объектов:")
del obj1
del obj2

print("\nПрограмма завершена.")