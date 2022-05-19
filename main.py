from pprint import pprint
import os

full_path = os.path.join(os.getcwd(), 'recipes.txt')

def cook_book_func():
    with open(full_path, encoding="utf-8") as recipes_file:
        cook_book = {}
        bludo = recipes_file.readline().strip()
        for intes in recipes_file:
            inte = int(intes.strip())
            ingri = []
            for ingridients in range(inte):
                data = recipes_file.readline().strip().split(' | ')
                ingri.append({'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]})
            cook_book[bludo] = ingri
            recipes_file.readline()
            bludo = recipes_file.readline().strip()
        return cook_book

# pprint(cook_book_func())
#
# print('\n')

def get_shop_list_by_dishes(dishes, person_count):
    book = cook_book_func()
    shop_list = {}
    for item in dishes:
        for ingredient in book[item]:
            name_ingr = ingredient['ingredient_name']
            if name_ingr in shop_list.keys():
                quantity = shop_list[name_ingr]['quantity'] + int(ingredient['quantity']) * person_count
                shop_list[name_ingr] = {'measure': ingredient['measure'], 'quantity': quantity}
            else:
                shop_list[name_ingr] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
    return shop_list

# pprint(get_shop_list_by_dishes(['Омлет','Омлет','Фахитос'], 2))
#



# print(name_file)


def cload_file():
    text_file = os.path.join(os.getcwd(), 'sorted')
    name_file = os.listdir(text_file)
    new_file = os.path.join(os.getcwd(), 'new_file.txt')
    full_text = {}
    for name in name_file:
        len_line = 0
        full_address_file = os.path.join(os.getcwd(), 'sorted', name)
        text = []
        # print(full_address_file)
        with open(full_address_file, encoding="utf-8") as recipes_file:
            for line in recipes_file:
                len_line += 1
                text.append(line.strip())
                # print(line.strip())
        full_text[len_line] = {'number' : len_line, 'name' : name, 'text': text}
    # pprint(full_text)
    with open(new_file, 'w', encoding="utf-8") as file_obj:
        for text_new in sorted(full_text):
            number = full_text[text_new]['number']
            name = ''.join(full_text[text_new]['name'].strip().split())
            text = '\n'.join(full_text[text_new]['text'])
            file_obj.write(f'{name} \n {number} \n {text} \n\n')

cload_file()





