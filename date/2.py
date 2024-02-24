import datetime

t_now = datetime.date.today()
dt = datetime.timedelta(days=1)
t_tomor = t_now + dt
t_yester = t_now - dt

print(f"{t_now }\n{t_tomor }\n{t_yester}" )