num=int(input('Enter the number: '))
i=2
while i<num:
    if num%i==0:
        print('This is not a prime number.')
        break
    i=i+1;
else:
    print('Prime number.')