import datetime

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)
print(x.strftime("%A"))

# %a abbreviated weekday name
# %A full weekday name
# %w weekday as a number 0-6, 0 is Sunday
# %d day of the month as a number
# %b abbreviated month name
# %B full month name
# %m month as a number
# %y year, two digits
# %Y year
# %H hour (24-hour clock) as a number
# %I hour (12-hour clock) as a number
# %p AM or PM
# %M minute as a number
# %S second as a number
# %f microsecond as a number
# %z timezone offset
