import time

for x in range(100):
    print(x)
    time.sleep(2)
import random

sen='Hello world hallo'
print(sen.index('o'))
print(sen.rindex('o'))# return the last o in the string
sen1=sen[sen.index('o')+1:]
print(sen1.index('o')+sen.index('o')+1)

for i in range(len(sen)):
    if sen[i] =='o':
        print(i)
lst=[1,5,7,8,100]
print(max(lst))
max=0
for ta in lst:
    if max < ta:
        max= ta
print(max)
numbers=list(range(100,1,-4))
print(numbers)
print('hungry Calc')
name = input('hii plese enter your name : ')
random.randint()
for x in range(10):
    print(random.randint(0,5))
# תוכנית שבודקת שהלקוח ניחש את המספר הראנדומאלי
while True:
    userGuess=int(input('please enter your lucky number '))
    v=random.randint(1,7)
    print(f'{userGuess} !!!!!! {v}')
    if  userGuess==v:
        print('we have a winner ')
        break
    print('try again')
for x in range(50):
    print(random.uniform(0,37))












