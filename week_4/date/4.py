from datetime import datetime

date_1 = input("Введите первую дату в формате YYYY-MM-DD HH:MM:SS: ")
date_2 = input("Введите вторую дату в формате YYYY-MM-DD HH:MM:SS: ")

date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date_1, date_format)
date2 = datetime.strptime(date_2, date_format)

time_diff = abs((date2 - date1).total_seconds())
print("Разница между датами в секундах:", time_diff)