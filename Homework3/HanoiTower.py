def hanoi_towers(size, src, dst, f):
    if size == 1:
        message = f"Диск 1 переложили c {src} на {dst}\n"
        f.write(message)
        print(message) 
    else:
        buf = 6 - src - dst
        hanoi_towers(size - 1, src, buf, f)

        message = f"Диск {size} переложили c {src} на {dst}\n"
        f.write(message)
        print(message)

        hanoi_towers(size - 1, buf, dst, f)


def main():
    # Ввод начальных условий
    try:
        num_disks = int(input("Введите количество дисков: "))
        if num_disks <= 0:
            raise ValueError("Кол-во дисков должно быть положительным.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return

    with open("Решение.txt", "w") as f:
        hanoi_towers(num_disks, 1, 3, f)

    print("Решение записано в файл 'Решение.txt'")

if __name__ == "__main__":
    main()