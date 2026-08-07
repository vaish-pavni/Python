#CALCULATOR
num1=float(input('Enter your first number: '))
num2=float(input('Enter your second number: '))

print('Calculator')

print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

choice = input('Enter your choice (1,2,3,4): ')

if choice == "1":
    print("Result=",num1+num2)
elif choice == "2":
    print("Result =",num1 - num2)
elif choice == "3":
    print('Result =', num1 * num2)
elif choice == "4":
    print('Result =', num1 / num2)
else:
    print('Invalid Choice')