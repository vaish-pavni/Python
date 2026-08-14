"""a=int(input('Enter first number:'))
b=int(input('Enter second number:'))

if a>b:
    print(a, 'is greater')
else:
    print(b, 'is greater')
"""


"""a=int(input('Enter your first number: '))
b=int(input('Enter your second number: '))
c=int(input('Enter your third number: '))

if a>b and a>c:
    print('a is greater',a)
elif b>a and b>c:
    print('b is greatest',b)
else:
    print('c is greatest',c)
"""



"""a=int(input('Enter your number: '))
if a%15==0:
    print('FIZZBUZZ')
elif a%3==0:
    print('FIZZ')
elif a%5==0:
    print('BUZZ')
else:
    print('invalid number')"""



"""for a in range(1,11):
    print(a)"""

"""for i in range (5, 31,2):
    print(i,end=' ')"""


"""i=1
while i<=11:
    print(a*i)
    i=i+1;
"""
"""i=5
while i<=31:
    print(i)
    i=i+2  
"""

"""start=int(input('enter the starting of series:'))
end=int(input('Enter the end of the series:'))
while start<=end:
    print(start , end=' ')
    start= start+2

a=5
b='xyz'
print(a*5)
print(b*5)"""


"""num=int(input('Enter your number: '))
fact = 1
for i in range (1, num+1):
    fact = fact * i

    print('Factorial of ',num,'is',fact)"""


"""num=int(input('Enter the number: '))
i=2
while i<=num:
    if num%i==0:
        i=i+1;
        print('prime number.')
    else:
        print('Not a prime number.')
"""

"""count = 0
for i in range (1,a+1):
    if a%i == 0:
        count += 1
    if count == 2:
        print('prime number.')
    else:
        print('not a prime number.')""" 

"""reversed = 0
while num>0:
    rem=num%10 '''remainder'''
    rev=rev*10+rem
    num=num//10
if number==rev:
    print('is a palindrome')
else:
    print('not a palindrome')"""


"""total_days = int(input('Enter number of days: '))

rem_days= total_days%365

month = rem_days//30
print('months = ',month)

rem_mdays=rem_days%30
week=rem_mdays//7

print('week=',week)

day=rem_mdays%7
print('day=',day)"""



"""num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

print('sum')
if(num1>=0 and num2 >= 0):
    print('RESULT=',num1+num2)
else:
    print('RESULT IS NOT APPLICABLE.')"""


"""num = int(input('Enter your number: '))

reversed=0

while num>0:
    rem = num % 10
    reversed = reversed * 10 + rem
    num = num // 10
print('reversed number = ',reversed)"""



"""num = int(input('Enter the number: '))
i=2
while i<=num:
    if num%i == 0:
        i=i+0%i
        print('PRIME NUMBER.')
    else:
        print('NOT A PRIME NUMBER.')"""


"""P=float(input('Enter Principle Amount : '))
R=float(input('Enter Rate of interest : '))
T=float(input('Enter Time (in years) : '))

si = (P*R*T)/100

print('Simple Interest:',si)"""


"""num = 2
while num<=100:
    i = 2

    while i < num:
        if num%i==0:
            break
        i=i+1
    if i == num:
        print(num)

    num = num + 1"""


"""a = int(input('Enter the number : '))
largest = 0

while a>0:
    digit = a % 10

    if digit > largest:
        largest = digit

    a = a // 10
print('largest digit = ', largest)"""

"""a=eval(input('enter the value : '))
print(type(a))"""


