from datetime import datetime

date_formats = {
    "The Moscow Times": "%A, %B %d, %Y",
    "The Guardian": "%A, %d.%m.%y",
    "Daily News": "%A, %d %B %Y"
}


def convert_date(date_str):
    for format_name, date_format in date_formats.items():
        try:
            date_obj = datetime.strptime(date_str, date_format)
            print(f"{format_name}: {date_obj}")
            return date_obj
        except ValueError:

            continue

    print("Формат даты не распознан.")
    return None


print("Введите дату или 'exit' для завершения программы:")
while True:
    user_input = input("Введите дату: ")
    if user_input.lower() in ["exit", "q"]:
        print("Программа завершена.")
        break
    convert_date(user_input)
