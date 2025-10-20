file_name = input("File Name: ")

if '.' not in file_name:
    print("application/octet-stream")
else:
    l = file_name.split('.')
    extension = l[-1]
    extension = extension.lower().strip()
    if extension == "gif":
        print("image/gif")
    elif extension == "jpg" or extension == "jpeg":
        print("image/jpeg")
    elif extension == "png":
        print("image/png")
    elif extension == "txt":
        print("text/plain")
    elif extension == "zip":
        print("application/zip")
    elif extension == "pdf":
        print("application/pdf")
    else:
        print("application/octet-stream")