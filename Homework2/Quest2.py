def create_pairs(boys, girls):
    # Сортируем списки
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)

    # Проверяем, равны ли длины списков
    if len(boys_sorted) != len(girls_sorted):
        print("Количество юношей и девушек не совпадает. Пары не могут быть созданы.")
        return

    # Создаем пары
    pairs = []
    for i in range(len(boys_sorted)):
        pairs.append((boys_sorted[i], girls_sorted[i]))

    # Выводим результат
    print("Идеальные пары:")
    for boy, girl in pairs:
        print(f"{boy} и {girl}")

# Пример списков
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

create_pairs(boys, girls)