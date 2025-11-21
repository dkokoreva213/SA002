# Функция для ввода слова, которое должно содержать только строчные английские буквы
def input_english_word():
    while True:
        s = input("Введите 1 слово (или 'exit' для выхода): ").strip()
        if s.lower() == 'exit':  # если ввели 'exit' — завершаем цикл
            return None
        if all('a' <= char <= 'z' for char in s):
            return s
        else:
            print("Некорректный ввод. Используйте только строчные английские буквы (a-z).")
# Функция для группировки списка слов по анаграммам
def group_anagrams(words):
    groups = {}
    # Создаём пустой словарь для хранения групп анаграмм

    for word in words:
        key = ''.join(sorted(word))
        # Сортируем буквы в слове по алфавиту, чтобы получить ключ группы анаграмм
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

# Основной алгоритм
words = []
while True:
    word = input_english_word()
    if word is None:
        break
    words.append(word)

result = group_anagrams(words)

print("\nГруппы анаграмм:")
for group in result:
    print(group)
