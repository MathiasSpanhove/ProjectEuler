__author__ = 'Mathias'

import timeit


class BidirectionalDict(dict):
    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        dict.__setitem__(self, val, key)


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

week_dict = BidirectionalDict()
for i, day in enumerate(days):
    week_dict[day] = i

month_dict = {}
for month in months:
    if month == "September" or "April" or "June" or "November":
        month_dict[month] = 30
    elif month == "February":
        month_dict[month] = 28
    else:
        month_dict[month] = 31


def given_day_X_after_Y_days_it_is(x, y):
    week_nb = week_dict.get(x)
    new_week_nb = (y + week_nb) % 7
    return week_dict.get(new_week_nb)


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


start = timeit.default_timer()

start_day = "Monday"
start_year = 1900
end_year = 2000

curr_day = start_day
curr_year = start_year
total_sundays = 0
while curr_year <= end_year:
    for month in months:
        if month == "February" and is_leap_year(curr_year):
            curr_day = given_day_X_after_Y_days_it_is(curr_day, month_dict.get(month) + 1)
        else:
            curr_day = given_day_X_after_Y_days_it_is(curr_day, month_dict.get(month))

        if curr_year != 1900 and curr_day == "Sunday":
            total_sundays += 1

    curr_year += 1

print(total_sundays)

print(timeit.default_timer() - start)
