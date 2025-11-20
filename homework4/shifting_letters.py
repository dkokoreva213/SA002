def shifting_letters(s, shifts):
    n = len(s)
    total_shift = 0
    res = []

    # Проходим с конца строки к началу
    for i in range(n - 1, -1, -1):
        total_shift = (total_shift + shifts[i]) % 26  # Оптимизация для больших чисел
        # Вычисляем новый символ с учетом сдвига
        new_char_code = (ord(s[i]) - ord('a') + total_shift) % 26 + ord('a')
        res.append(chr(new_char_code))

    return ''.join(res[::-1])


# Блок для ввода данных пользователем
while True:
    s = input("Введите строку из букв (только строчные английские буквы): ")

    # Проверяем длину строки (1 <= s.length <= 10^5)
    if len(s) < 1 or len(s) > 10 ** 5:
        print(f"Длина строки должна быть от 1 до {10 ** 5} символов. Попробуйте еще раз.")
        continue

    # Проверяем, что все символы - строчные английские буквы
    if all('a' <= char <= 'z' for char in s):
        break
    else:
        print("Некорректный ввод. Используйте только строчные английские буквы (a-z).")

# Ввод сдвигов
while True:
    shifts_input = input("Введите сдвиги для каждой буквы через пробел: ")
    shifts = list(map(int, shifts_input.split()))

    # Проверяем, что длины совпадают
    if len(s) != len(shifts):
        print(f"Ошибка: количество сдвигов ({len(shifts)}) должно совпадать с длиной строки ({len(s)}).")
        continue

    # Проверяем диапазон сдвигов (0 <= shifts[i] <= 10^9)
    if all(0 <= x <= 10 ** 9 for x in shifts):
        break
    else:
        print("Сдвиги должны быть в диапазоне от 0 до 1 000 000 000.")

# Вычисляем и выводим результат
result = shifting_letters(s, shifts)
print("Результат сдвига:", result)