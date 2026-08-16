unit = input('Is The Temperature in Celsius or Fahrenheit(C/F) : ')
Temp = float(input('Enter the temperature : '))

if unit=='C':
    temp=round((9*Temp)/5+32 , 1)
    print(f"The temperature in Fahrenheit is = {temp} degree Fahrenheit.")
elif unit=='F':
    temp=round((Temp-32)*5/9, 1)
    print(f"The temperature in Celsius is = {temp} degree Celsius.")
else:
    print(f"{unit} is an invalid unit of tempeture.")