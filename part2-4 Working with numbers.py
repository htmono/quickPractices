
kerrat = 0
summa = 0
keski = 0
posit = 0
negat = 0
while True:
    print("Please type in integer numbers. Type in 0 to finish.")
    numero = int(input("Number: "))
    if numero == 0:
        break
    else:
        kerrat = kerrat + 1
        summa = summa + numero
        if numero > 0:
            posit = posit + 1
        else:
            negat = negat + 1

keski = summa / kerrat
print(f"Numbers typed in {kerrat}")
print(f"The sum of the numbers is {summa}")
print(f"The mean of the numbers is {keski}")
print(f"Positive numbers {posit}")
print(f"Negative numbers {negat}")