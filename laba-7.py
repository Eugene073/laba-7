class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


class Girl:
    def __init__(self, name):
        self.name = name


class DessertCombination:
    def __init__(self, desserts, girls):
        self.desserts = desserts
        self.girls = girls
        self.combinations = []
        self.filtered_combinations = []
        self.min_calories = []
        self.max_calories = []

    def generate_combinations(self):
        for i in range(len(self.desserts)):
            for j in range(len(self.desserts)):
                for k in range(len(self.desserts)):
                    combination = [self.desserts[i], self.desserts[j], self.desserts[k]]
                    if combination not in self.combinations:
                        self.combinations.append(combination)

    def filter_combinations(self, max_calories):
        self.filtered_combinations = [combination for combination in self.combinations
                                      if sum(dessert.calories for dessert in combination) <= max_calories]

    def find_extreme(self, func, mode):
        if mode == "min":
            extreme = min(self.filtered_combinations, key=func)
        elif mode == "max":
            extreme = max(self.filtered_combinations, key=func)
        return extreme

    def calorie_count(self, combination):
        count = 0
        for dessert in combination:
            count += dessert.calories
        return count

    def calculate_combinations(self, max_calories):
        self.generate_combinations()
        self.filter_combinations(max_calories)
        self.filtered_combinations = sorted(self.filtered_combinations, key=self.calorie_count)
        self.min_calories = self.find_extreme(self.calorie_count, "min")
        self.max_calories = self.find_extreme(self.calorie_count, "max")

    def print_combinations(self):
        count = len(self.filtered_combinations)
        for i, combination in enumerate(self.filtered_combinations):
            print("Вариант №", i + 1, "- калорийность:", self.calorie_count(combination))
            for girl, dessert in zip(self.girls, combination):
                print(girl.name, 'будет есть', dessert.name, '({} ккал)'.format(dessert.calories))
            print('-' * 20)
        print("Итоговое количество вариантов:", count)
        print('-' * 20)

    def print_extreme_calories(self):
        print("Самый низкий уровень калорийности:")
        print("Калорийность:", self.calorie_count(self.min_calories))
        for girl, dessert in zip(self.girls, self.min_calories):
            print(girl.name, 'будет есть', dessert.name, '({} ккал)'.format(dessert.calories))
        print('-' * 20)

        print("Самый высокий уровень калорийности:")
        print("Калорийность:", self.calorie_count(self.max_calories))
        for girl, dessert in zip(self.girls, self.max_calories):
            print(girl.name, 'будет есть', dessert.name, '({} ккал)'.format(dessert.calories))
        print('-' * 20)


dessert_data = [('десерт №1', 200),
                ('десерт №2', 300),
                ('десерт №3', 150),
                ('десерт №4', 250),
                ('десерт №5', 350),
                ('десерт №6', 180),
                ('десерт №7', 280),
                ('десерт №8', 220),
                ('десерт №9', 320),
                ('десерт №10', 120)]

girl_data = ['1-ая девушка', '2-ая девушка', '3-ая девушка']

desserts = [Dessert(name, calories) for name, calories in dessert_data]
girls = [Girl(name) for name in girl_data]

max_calories = int(input("Введите максимальное количество калорий(минимум 360, максимум 1050): \n"))
if max_calories < 360:
    print("Извините, мы не можем предоставить вам комбинацию из десертов суммарной калорийностью менее 360\n")
    print("Вот наша самая низкокалорийная комбинация:\n")
    max_calories = 360
    dessert_combination = DessertCombination(desserts, girls)
    dessert_combination.calculate_combinations(max_calories)
    dessert_combination.print_combinations()
    exit()

if max_calories > 1050:
    dessert_combination = DessertCombination(desserts, girls)
    dessert_combination.calculate_combinations(max_calories)
    dessert_combination.print_combinations()
    dessert_combination.print_extreme_calories()
    print("Извините, мы не можем предоставить вам комбинацию из десертов суммарной калорийностью более 1050\n")
    exit()

dessert_combination = DessertCombination(desserts, girls)
dessert_combination.calculate_combinations(max_calories)
dessert_combination.print_combinations()
dessert_combination.print_extreme_calories()