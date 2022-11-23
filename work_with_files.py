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
            ingredients.append({'ingr_name': ingr_name, 'quantity': int(quantity), 'measure': measure})
        f.readline()
        menu[dish] = ingredients
    pprint(menu)

dishes_list = []
for key in menu.keys():
    dishes_list.append(key)
print(f'В меню входит: {", ".join(dishes_list)}')


def get_shop_list_by_dishes(dishes, person):
    shop_list = {}
    for key, value in menu.items():
        if key.lower() in dishes:
            for dish in value:
                dish['quantity'] *= person
                ingr = dish.pop('ingr_name')
                if ingr not in shop_list.keys():
                    shop_list[ingr] = dish
                else:
                    shop_list[ingr]['quantity'] += shop_list[ingr]['quantity']
    return pprint(shop_list)


dishes = input('Что бы вы хотели заказать?. (Названия указывать через запятую): ').lower().strip().split(',')
person_count = int(input('Введите количество персон: '))
get_shop_list_by_dishes(dishes, person_count)
