#function method
import math


def printHii():
    '''
    this func print hii without recive any variables
    :return: none
    '''
    print('hii')
# function can work with loops
def printHiiThreeTimes():
    for i in range(3):
        printHii()
    return

def printName(x):
    print(f'hiii {x}')
#printHii()
#printHiiThreeTimes()
printName('lidor')
name='soso'


def hodiLen(yuyu):
    count=0
    for lt in yuyu:
        count+=1
    print(count)

print(len('Donland trump'))
hodiLen(yuyu='yuyu')
hodiLen('Donland trump')
str='lidor seri'
hodiLen(str)

def printFullName(fname,lname):
    print(f'hii {fname} {lname}')

first ='guy'
last='bnenenson'
printFullName(first,last)
printFullName(last,first)
printFullName('hodi',last)
printFullName(input('first name :'),last)
printFullName(input('first name :'),input('lastname:'))
printFullName(lname=last,fname=first)'''
'''def printKidsName(*kidName):
    for x in kidName:
        print(x)
    print(kidName[1])

printKidsName(['hodi','beni'],'or','dor')

def getCircleArea(radius):
    area= 3.14 * radius**2
    return area
    print('wooooooooooow')
carea=getCircleArea(3)
print(carea*3)

x=3
y=getCircleArea(5)

def getMultiNumbers(c=None,a=10,b=6.0):
    return  a*b

x= int(input('1 number '))
y= int(input('1 number '))
z=getMultiNumbers(3,x)
print(type(z))
print(z)

def foo():
    #TODO:
    pass









