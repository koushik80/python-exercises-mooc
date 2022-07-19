# E-6.1.8: Recipe search

# Problem: https://programming-22.mooc.fi/part-6/1-reading-files#programming-exercise-recipe-search


# Sample output:


# Solution:

def search_item(file: str):
    recipes = {}
    recipes_list = []

    with open(file) as recipe_file:
        for line in recipe_file:
            line = line.replace('\n', '')
            recipes_list.append(line)
            if len(line) > 0:
                recipes[recipes_list[0]] = recipes_list[1:]
            else:
                recipes_list = []

    return recipes


def search_by_name(filename: str, word: str):
    recipes = search_item(filename)
    recipe_names = []
    searched_recipe_names = []

    for recipe, raw_ingrd in recipes.items():
        recipe_names.append(recipe)

    for res_name in recipe_names:
        if word.lower() in res_name.lower():
            searched_recipe_names.append(res_name)

    return searched_recipe_names


def search_by_time(filename: str, prep_time: int):
    recipes = search_item(filename)
    name_and_time = []

    for res_name, res_data in recipes.items():
        if prep_time >= int(res_data[0]):
            name_and_time.append(
                f'{res_name}, preparation time {res_data[0]} min')

    return name_and_time


def search_by_ingredient(filename: str, ingredient: str):
    recipes = search_item(filename)
    list = []

    for recipe, desc in recipes.items():
        if ingredient in desc:
            list.append(f'{recipe}, preparation time {desc[0]} min')

    return list


if __name__ == '__main__':
    search_result = search_by_name("recipes1.txt", "Meatballs")

    for name in search_result:
        print(name)

    search_result = search_by_time("recipes1.txt", 45)

    for desc in search_result:
        print(desc)

    search_result = search_by_ingredient("recipes1.txt", "Cake pops")

    for recipe in search_result:
        print(recipe)
