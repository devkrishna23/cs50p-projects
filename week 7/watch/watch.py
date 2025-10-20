import re

def main():
    print(parse(input("HTML: ")))


def parse(html):
    pattern = r'<iframe[^>]*src="(?:https|http)://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+?)"'
    search = re.search(pattern, html)
    if search:
        link = search.group(1)
        return f"https://youtu.be/{link}"
    else:
        return None

if __name__ == "__main__":
    main()