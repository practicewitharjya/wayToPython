with open("currencyConverter.txt") as f:
    # print(f.readlines())
    for item in f.readlines():
        # print(item)
        currency = item.split('\t')
        # print(currency)
        if currency[0] == "Canadian Dollar":
            print(f"1 INR = {currency[1]} Canadian Dollar")