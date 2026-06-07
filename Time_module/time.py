import datetime

date = datetime.date(2020, 5, 6)
today = datetime.date.today()
print(date, today)

time = datetime.time(11, 20, 2)
now = datetime.datetime.now()
print(time, now)

now1 = now.strftime("%a")
print(now1)