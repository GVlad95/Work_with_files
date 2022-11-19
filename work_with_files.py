from pprint import pprint
with open('recipes.txt', 'rt', encoding='utf8') as f:
    menu = {}
    for line in f:
        dish = line.strip()
        ingr_count = int(f.readline())
        ingredients = []
        for i in range(ingr_count):
            ingr = f.readline().strip().split('|')
            ingr_name, quantity, measure = ingr
            ingredients.append({'ingr_name': ingr_name, 'quantity': quantity, 'measure': measure})
        f.readline()
        menu[dish] = ingredients
print(menu)
