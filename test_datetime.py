import datetime
import pytz

today = datetime.date.today()
print(today)
print(today.month)
print(today.day)
print(today.weekday())

birthday = datetime.date(1996, 10, 24)
print(birthday)

#get the number of days I have been alive in days
days_since_birth = (today-birthday).days

print(days_since_birth)

#adding number of days to today => add and subtract dates using timedelta
tdelta = datetime.timedelta(days=10)
print(today + tdelta)

#printing hours, minutes, seconds and milliseconds
print(datetime.time(6, 10, 50,30))
# datetime.date(Y, M, D)
# datetime.time(h, m, s, ms)
# datetime.datetime(Y, M, D, h, m, s, ms)

#adding 10hours to current time
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

#setting different timezone
datetime_today =datetime.datetime.now(tz=pytz.UTC)
datetime_africa = datetime_today.astimezone(pytz.timezone('Africa/Douala'))
print(datetime_africa)

#getting list of timezone
for tz in pytz.all_timezones:
    print(tz)
    
#string formatting with dates
# 2020-11-25 to November 25, 2020
# using strftime where f= formating

print(datetime_africa.strftime('%B %d,%Y')) #%B for the month, %d for the day and %Y for the year

#converting from November 25, 2020 to datetime(2020,11,25)
#using strptime where p = parsing
datetime_thing= datetime.datetime.strptime('November 25, 2020', '%B %d, %Y')
print(repr(datetime_thing))