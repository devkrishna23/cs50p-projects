import requests, sys

api = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=8591b8ded539031fd101f5f54a5df0a3d971d661e307dc0c6340b1ebe867e6f4"

argv = sys.argv

n = len(argv)

if n != 1:
    try:
        number = float(argv[1])
        try:
            r = requests.get(api)
            d = r.json()
            price = float(d["data"]["priceUsd"])
            amount = number * price
            print(f"${amount:,.4f}")
            sys.exit(0)
        except requests.RequestException:
            sys.exit(1)

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)