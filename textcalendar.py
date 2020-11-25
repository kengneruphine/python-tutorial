import calendar

#print the days of the week, limit 3 xters
print(calendar.weekheader(3))
print()

#first day of the week starts from 0
print(calendar.firstweekday())

#printing this month calender
print(calendar.month(2020,11))

#print the month calendar in matrix format
print(calendar.monthcalendar(2020,11))

#print the calendar for this year
print(calendar.calendar(2020))

#print day of the week passing in the year, month and date of today
day_of_the_week= calendar.weekday(3020, 11, 23)
print(day_of_the_week)

#checking if year is a leap year
is_leap = calendar.isleap(2020)
print(is_leap)

#print the number of leap days in a range of years (exclusive)
how_many_leap_days = calendar.leapdays(2000, 2020)
print(how_many_leap_days)

digits = [1,2,3,4,5,6,7,8,9,0]

#striding => keeping 2 steps
print(digits[0:10:2])

#method for reversing a list
print(digits[::-1])

#unpacking tuples
person=("John", 25, "Pizza")
(name, age, favfood) = person
print(name)
print(age)