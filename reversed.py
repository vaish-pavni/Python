num = int(input('Enter your number: '))

reversed=0

while num>0:
    rem = num % 10
    reversed = reversed * 10 + rem
    num = num // 10
print('reversed number = ',reversed)