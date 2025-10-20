import re


def main():
    print(convert(input("Hours: ")))

def convert(text):

    pattern = r"((?:[1-9]|1[0-2])(?:\:[0-5][0-9])?) ((?:AM|PM)) to ((?:[1-9]|1[0-2])(?:\:[0-5][0-9])?) ((?:AM|PM))"
    search = re.search(pattern, text)
    if search:
    
        start_time, ante1, end_time, ante2 = search.groups()

        
        if ":" in start_time:
            hour1, minutes1 = remove_semi(start_time)
        else:
            hour1 = start_time
            minutes1 = "00"

        if ":" in end_time:
            hour2, minutes2 = remove_semi(end_time)     
        else:
            hour2 = end_time
            minutes2 = "00"

        new_hour1 = (twelve_to_twentyfour(hour1,ante1))
        new_hour2 = (twelve_to_twentyfour(hour2,ante2))
        new_time1 = f"{new_hour1:02}:{int(minutes1):02}"
        new_time2 = f"{new_hour2:02}:{int(minutes2):02}"

        return f"{new_time1} to {new_time2}"
        

    else:
        raise ValueError("incorrect time format")


def twelve_to_twentyfour(time,M):

            if time == "12" and M == "AM":
                return int(time) - 12
            elif time == "12" and M == "PM":
                return int(time)
            elif M == "PM":
                return int(time) + 12
            elif M == "AM":
                return int(time)

def remove_semi(s):
    a,b = s.split(':')
    return a,b

if __name__ == "__main__":
    main()