import validators

email = input("What's your email address? ")

valid_or_invalid = validators.email(email)

if valid_or_invalid == True:
    print("Valid")
else:
    print("Invalid")