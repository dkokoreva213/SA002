def min_sum_of_pairs(num: int) -> int:
    num_str = str(num)
    min_sum = float('inf')
    for i in range(1, len(num_str)):
        part1 = int(num_str[:i])
        part2 = int(num_str[i:])
        current_sum = part1 + part2
        if current_sum < min_sum:
            min_sum = current_sum
    return min_sum


while True:
    user_input = input("Введите четырехзначное число: ")
    if len(user_input) == 4:
        num = int(user_input)
        break

result = min_sum_of_pairs(num)
print("Минимальная сумма:", result)
