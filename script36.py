class Animals:
    def __init__(self, name):
        self.name = name
class Birds(Animals):
    def __init__(self, name, color, habitat, wingspan, diet ):
        super().__init__(name)
        self.color = color
        self.habitat = habitat
        self.wingspan = wingspan
        self.diet = diet
class Mammals(Animals):
    def __init__(self, name, color, habitat, size, diet):
        super().__init__(name)
        self.color = color
        self.habitat = habitat
        self.size = size
        self.diet = diet
class Reptiles(Animals):
    def __init__(self, name, habitat, scale_size, size, diet):
        super().__init__(name)
        self.habitat = habitat
        self.scale = scale_size
        self.size = size
        self.diet = diet
class Fish(Animals):
    def __init__(self, name, color, habitat, diet):
        super().__init__(name)
        self.color = color
        self.habitat = habitat
        self.diet = diet

# Птицы (Birds)
eagle = Birds(name="Орел", color="Коричневый", habitat="Горы", wingspan="2 метра", diet="Хищник")
chicken = Birds(name="Курица", color="Белая", habitat="Ферма", wingspan="0.5 метра", diet="Зерно")

# Млекопитающие (Mammals)
rat = Mammals(name="Крыса", color="Серая", habitat="Город", size="Маленький", diet="Всеядное")
monkey = Mammals(name="Обезьяна", color="Коричневая", habitat="Джунгли", size="Средний", diet="Фрукты")

# Рептилии (Reptiles)
snake = Reptiles(name="Змея", habitat="Пустыня", scale_size="Мелкая", size="Длинный", diet="Хищник")
chameleon = Reptiles(name="Хамелеон", habitat="Лес", scale_size="Средняя", size="Маленький", diet="Насекомые")

# Рыбы (Fish)
clownfish = Fish(name="Рыба-клоун", habitat="Океан", color="Оранжевый", diet="Планктон")
white_shark = Fish(name="Белая акула", habitat="Океан", color="Серый", diet="Хищник")



