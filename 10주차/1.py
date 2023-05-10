'''import random

print("random.randint(10,100)", random.randint(10,100))
#as를 사용하면 math를 생략해서 사용가능
import math as m

#리스트 안에 있는 숫자를 다 더함 float형으로 나옴
a = m.fsum([1,1,1,1,1,1,1]) 
print(a)
print("+".center(11,"="))

#10의 3승 float형
a = m.pow(10,3)
print(type(a)) 
print("+".center(11,"="))

#as는 별명
from math import pow as p

print(p(10,3))
print("+".center(11,"="))

from math import pow,fsum

print(pow(10,3))
print(fsum([1,1,1,1,1]))
print("+".center(11,"="))
'''
import def1 #import에서 파일 자체를 모두 실행 시킴
print("+".center(11,"="))
def1.helloya()