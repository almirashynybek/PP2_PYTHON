#1
import datetime

tday =  datetime.date.today()
tdelta = datetime.timedelta(days=5)

print(tday - tdelta)

#date2 = date1 + timedelta
# timedelta = date1 + date2


#2
import datetime

t_now = datetime.date.today()
dt = datetime.timedelta(days=1)
t_tomor = t_now + dt
t_yester = t_now - dt

print(f"{t_now }\n{t_tomor }\n{t_yester}" )


#3
import datetime
dt = datetime.datetime.today()
print(dt.strftime("%f"))


#4
import datetime

today = datetime.date.today()
birth_day = datetime.date(2024,8,21)
till_birth = birth_day - today

print(till_birth.total_seconds())
