import sys
from PIL import Image, ImageOps

n = len(sys.argv)

if n > 3:
    sys.exit("Too many command-line arguments")
elif n < 3:
    sys.exit("Too few command-line arguments")
else:
    extensions = ("png", "jpg", "jpeg")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not input_file.endswith(extensions):
        sys.exit("Not an image file")
    elif not output_file.endswith(extensions):
        sys.exit("Invalid output")
    else:
        extension1 = input_file.rsplit('.')[-1].lower()
        extension2 = output_file.rsplit('.')[-1].lower()
        if extension1 != extension2:
            sys.exit("Input and output have different extensions")
        else:
            try:
                image = Image.open(input_file)
            except  FileNotFoundError:
                sys.exit("Input does not exist")
            try: 
                shirt = Image.open("shirt.png")
            except FileNotFoundError:
                sys.exit("shirt.png does not exist")
            
            size = shirt.size
            image = ImageOps.fit(image, size)
            image.paste(shirt, (0,0), shirt)
            image.save(output_file)
    
    
