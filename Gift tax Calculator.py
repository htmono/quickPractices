giftValue = int(input("Value of gift: "))
taxAmount = 0
if giftValue < 5000:
    taxAmount = 0
    print("No tax!")

elif giftValue >= 5000:
    if giftValue >= 5000 and giftValue < 25000:
        taxAmount = 100 + (giftValue - 5000) * 0.08
    elif giftValue >= 25000 and giftValue < 55000:
        taxAmount = 1700 + (giftValue - 25000) * 0.1
    elif giftValue >= 55000 and giftValue < 200000:
        taxAmount = 4700 + (giftValue - 55000) * 0.12
    elif giftValue >= 200000 and giftValue < 1000000:
        taxAmount = 22100 + (giftValue - 200000) * 0.15
    elif giftValue >= 1000000:
        taxAmount = 142100 + (giftValue - 1000000) * 0.17

if taxAmount > 0:
    print(f"Amount of tax: {taxAmount} euros")

