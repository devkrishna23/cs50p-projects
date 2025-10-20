import sys, random
from pyfiglet import Figlet

figlet = Figlet()

l = figlet.getFonts()
n1 = len(l)

l1 = sys.argv
n = len(l1)

if n != 1:
    if l1[1] != '-f':
        print("Invalid usage")
        sys.exit(1)
    else:
        if l1[2] not in l:
            print("Usage: python figlet.py -f fontname")
            sys.exit(1)
        else:
            text = input("Input: ")
            fig_text = text
            figlet.setFont(font = l1[2])
            print(figlet.renderText(fig_text))
            sys.exit(0)
else:
    text = input("Input: ")
    fig_text = text
    ran = random.randint(0, n1-1)
    figlet.setFont(font = l[ran])
    print(figlet.renderText(fig_text))
    sys.exit(0)