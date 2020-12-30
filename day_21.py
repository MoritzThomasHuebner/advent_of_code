from copy import deepcopy

lines = []
with open('day_21_input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.replace('\n', ''))


class Meal(object):

    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens

    @classmethod
    def from_input_line(cls, line):
        data = line.split(' (')
        ingredients = data[0].split(' ')
        allergens = data[1].replace('contains ', '').replace(',', '').rstrip(')').split(' ')
        return cls(ingredients=ingredients, allergens=allergens)

    def remove_ingredient(self, ingredient):
        try:
            self.ingredients.remove(ingredient)
        except ValueError:
            pass

    def remove_multiple_ingredients(self, ingredients):
        for i in ingredients:
            self.remove_ingredient(i)


meals = [Meal.from_input_line(line) for line in lines]


all_ingredients = set()
all_allergens = set()
for meal in meals:
    for ingredient in meal.ingredients:
        all_ingredients.add(ingredient)
    for allergen in meal.allergens:
        all_allergens.add(allergen)

ingredients_with_possible_allergens = set()

for allergen in all_allergens:
    possible_ingredients = []
    for meal in meals:
        if allergen in meal.allergens:
            possible_ingredients.append(meal.ingredients)
    possible_ingredients = set.intersection(*[set(pa) for pa in possible_ingredients])
    ingredients_with_possible_allergens = ingredients_with_possible_allergens.union(possible_ingredients)
inert_ingredients = all_ingredients.difference(ingredients_with_possible_allergens)


counter = 0
for meal in meals:
    for nai in inert_ingredients:
        if nai in meal.ingredients:
            counter += 1

print(counter)
print()

for meal in meals:
    meal.remove_multiple_ingredients(inert_ingredients)

allergen_ingredients = dict()

while len(ingredients_with_possible_allergens) > 0:
    for allergen in all_allergens:
        possible_ingredients = deepcopy(ingredients_with_possible_allergens)
        for meal in meals:
            if allergen in meal.allergens:
                possible_ingredients = possible_ingredients.intersection(set(meal.ingredients))

        if len(possible_ingredients) == 1:
            i = list(possible_ingredients)[0]
            allergen_ingredients[allergen] = i
            ingredients_with_possible_allergens.remove(i)


canonical_dangerous_ingredients = [i for _, i in sorted(zip(list(allergen_ingredients.keys()), list(allergen_ingredients.values())))]
print(",".join(canonical_dangerous_ingredients))