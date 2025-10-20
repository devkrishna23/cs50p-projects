import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    octet = r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    pattern = rf"^(?:{octet}\.){{3}}{octet}$"

    return bool(re.match(pattern, ip))


if __name__ == "__main__":
    main()