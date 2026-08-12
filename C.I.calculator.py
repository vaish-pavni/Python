#PYTHON COMPOND INTEREST CALCULATOR

principle = float(input("Enter the principle amount: "))
while principle < 0:
    print("Your principle value can't be less than or equal to zero.")
    principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the Interest rate: "))
while rate < 0:
    print("Your Interest rate can't be less than or equal to zero.")
    principle = float(input("Enter the Interest rate: "))

time = int(input("Enter the time in years: "))
while principle < 0:
    print("Your principle value can't be less than or equal to zero.")
    principle = int(input("Enter the time in years: "))

total = principle * pow((1 + rate / 100),time)
print(f"Your compound interest is {total:.2f}")