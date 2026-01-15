from datetime import date
import re

BIRTHDAY_MONTH = 9
BIRTHDAY_DAY = 30

def unit(value, name):
    return f"{value} {name}" if value == 1 else f"{value} {name}s"

def add_months(d, months):
    year = d.year + (d.month - 1 + months) // 12
    month = (d.month - 1 + months) % 12 + 1
    day = min(d.day, [31,28,31,30,31,30,31,31,30,31,30,31][month - 1])
    return date(year, month, day)

today = date.today()
this_year_birthday = date(today.year, BIRTHDAY_MONTH, BIRTHDAY_DAY)
next_year_birthday = date(today.year + 1, BIRTHDAY_MONTH, BIRTHDAY_DAY)

delta = (this_year_birthday - today).days
output = None

if delta == 0:
    output = 'today <img src="assets/birthday.gif" height="18" style="vertical-align: middle;" />'

elif delta == 1:
    output = "tomorrow"
    
elif delta == -1:
    output = "birthday was: yesterday"

elif -7 <= delta < -1:
    output = "birthday was: a week ago"

elif delta < -7:
    target = next_year_birthday

    months = 0
    temp = today
    while add_months(temp, 1) <= target:
        temp = add_months(temp, 1)
        months += 1

    remaining_days = (target - temp).days
    weeks = remaining_days // 7
    days = remaining_days % 7

    output = (
        f"In {unit(months, 'month')} · "
        f"{unit(weeks, 'week')} · "
        f"{unit(days, 'day')}"
    )
    
else:
    target = this_year_birthday

    months = 0
    temp = today
    while add_months(temp, 1) <= target:
        temp = add_months(temp, 1)
        months += 1

    remaining_days = (target - temp).days
    weeks = remaining_days // 7
    days = remaining_days % 7

    if months > 0:
        output = (
            f"In {unit(months, 'month')} · "
            f"{unit(weeks, 'week')} · "
            f"{unit(days, 'day')}"
        )
    elif weeks > 0:
        output = f"{unit(weeks, 'week')} · {unit(days, 'day')}"
    else:
        output = unit(days, "day")
        
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

updated = re.sub(
    r"Birthday in:.*",
    f"Birthday in: {output}",
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
