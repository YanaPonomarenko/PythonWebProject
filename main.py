#1
fruits = ("яблуко", "банан", "яблуко", "апельсин", "банан", "яблуко", "груша")
search_fruit = input("Введіть назву фрукта: ")
print(f"Фрукт '{search_fruit}' зустрічається {fruits.count(search_fruit)} раз(ів).")

#2
manufacturers = ["Ford", "Chevrolet", "Tesla", "Ford", "Jeep", "Tesla", "Ford"]

print("Список:", manufacturers)

target = input("Введіть назву виробника для заміни: ")
replacement = input("Введіть слово для заміни: ")

for i in range(len(manufacturers)):
    if manufacturers[i] == target:
        manufacturers[i] = replacement
print("Новий список:", manufacturers)

#2
cities1 = {"Одеса", "Львів", "Київ", "Харків", "Дніпро"}
cities2 = {"Львів", "Одеса", "Миколаїв", "Київ"}

common = cities1 & cities2
print("Міста в обох множинах:", common)

#3
cities1 = {"Одеса", "Львів", "Харків", "Дніпро"}
cities2 = {"Львів", "Одеса", "Миколаїв", "Київ"}

only_in_first = cities1 - cities2
print("Є в першій,немає в другій:", only_in_first)

#
