a=int(input('Enter your number: '))
if a%15==0:
    print('FIZZBUZZ')
elif a%3==0:
    print('FIZZ')
elif a%5==0:
    print('BUZZ')
else:
    print('invalid number')