class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print('Чирик')

    def eat(self):
        print('Зерно')


class Mammal(Animal):
    def make_sound(self):
        print('Мууу')

    def eat(self):
        print('Трава')


class Reptile(Animal):
    def make_sound(self):
        print('Шшшш')

    def eat(self):
        print('Грызуны')


class ZooKeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f'{self.name} кормит {animal.name}')
        animal.eat()


class Veterinarian():
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f'{self.name} лечит {animal.name}')


class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк')

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f'Сотрудник {employee.name} добавлен в зоопарк')

    def delete_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f'Животное {animal.name} удалено из зоопарка')
        else:
            print(f'Животное {animal.name} не найдено в зоопарке')

    def delete_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f'Сотрудник {employee.name} удален из зоопарка')
        else:
            print(f'Сотрудник {employee.name} не найден в зоопарке')


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


animals = [
    Bird("Воробей", 2),
    Mammal("Корова", 5),
    Reptile("Змея", 3)
]
animal_sound(animals)

zoo = Zoo()
zoo.add_animal(Bird("Попугай", 4))
zoo.add_animal(Mammal("Лев", 7))
zoo.add_employee(ZooKeeper("Иван"))
zoo.add_employee(Veterinarian("Мария"))

keeper = ZooKeeper("Иван")
vet = Veterinarian("Мария")
lion = Mammal("Лев", 7)
keeper.feed_animal(lion)
vet.heal_animal(lion)