
tarina = ""
sana = ""
sana2 = ""
while True:
    sana = input("Please type in a word: ")
    if sana == "end":
        break
    elif sana2 == sana:
        break
    else:
        tarina = tarina + " " + sana
    sana2 = sana

print(tarina)