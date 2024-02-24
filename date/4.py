import datetime

today = datetime.date.today()
birth_day = datetime.date(2024,8,21)
till_birth = birth_day - today

print(till_birth.total_seconds())

#date2 = date1 +/- timedelta
# timedelta = date1 +/- date2