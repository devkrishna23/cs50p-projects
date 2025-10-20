months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        outdated = input("Date: ").strip()
        if ',' not in outdated:
            month, day, year = outdated.split('/')
            month = int(month)
            day = int(day)
            if 1 <= month <= 12 and 1 <= day <= 31 and year.isdigit():
                print(f"{year}-{(month):02}-{(day):02}")
                break
            
        else:
            if outdated[0].isalpha():
                month_day, year = outdated.split(',')
                month_day = month_day.strip()
                year = year.strip()
                month,day = month_day.split()
                day = int(day)
                if 1 <= day <= 31 and year.isdigit():
                    if month in months:
                        index = months.index(month) + 1
                        print(f"{year}-{index:02}-{int(day):02}")
                        break
    except:
        continue