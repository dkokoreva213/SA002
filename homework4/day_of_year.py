from datetime import datetime

def day_of_year(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.timetuple().tm_yday

# Просим пользователя ввести дату
user_date = input("Введите дату в формате YYYY-MM-DD: ")
result = day_of_year(user_date)
print("День года:", result)

