from datetime import date, timedelta
import re

BIRTHDAY_MONTH = 9
BIRTHDAY_DAY = 30

today = date.today()
this_year_birthday = date(today.year, BIRTHDAY_MONTH, BIRTHDAY_DAY)
next_year_birthday = date(today.year + 1, BIRTHDAY_MONTH, BIRTHDAY_DAY)

delta = (this_year_birthday - today).days

output = None

if delta == 0:
    output = 'today <img src="assets/birthday.webp" height="18" style="vertical-align: middle;" />'

elif delta == 1:
    output = "tomorrow"
  
elif 1 < delta < 7:
    output = f"{delta} days"
  
elif 7 <= delta < 30:
    weeks = delta // 7
    days = delta % 7
    output = f"{weeks} weeks · {days} days"

elif delta == -1:
    output = "birthday was: yesterday"
  
elif -7 <= delta < -1:
    output = "birthday was: a week ago"

else:
    if delta > 0:
        target = this_year_birthday
    else:
        target = next_year_birthday

    days_left = (target - today).days

    months = days_left // 30
    weeks = (days_left % 30) // 7

    output = f"In {months} months · {weeks} weeks"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

updated = re.sub(
    r"Birthday in:.*",
    f"Birthday in: {output}",
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
