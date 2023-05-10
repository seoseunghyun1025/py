'''
def irum(su1="hello", su2="world"):
    print("안녕!",su1,"안녕!", su2)
def sum(num1, num2):
    return num1 + num2

su = input()
su2 = input()
irum(su, su2)
irum()
result = sum(10,20)
print(result)
'''
'''
def mysum2(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result

print(mysum2(1,1,1,1,1,1,1,1,1,1))
lst1 = [10,10,10,10,10,10,10]
lst2 = [10,10,10,10,10,10,10,10,10,10,10]
tup = 1,2,3,4,5,6,
print(mysum2(*tup)) #인자의 수를 모를 때 *사용
print(mysum2(*lst1))
print(mysum2(*lst2))
'''
'''
key, value, pair
cafe function
메뉴 = 가격,
출력해주는 function을 만들자.
cafe(아메=2000, 라떼=3000, 핫초코=5000)
cafe(아메=2000, 라떼=3000)
cafe(아메=2000)
'''
'''
def cafe(**keyvalue):
    for key in keyvalue: #아메, 라떼, 핫초코
        print(key, keyvalue[key]) # 아메, 2000


cafe(아메=2000, 라떼= 3000, 핫초코=5000)
print("=".center(20,"="))
cafe(아메=2000, 라떼= 3000)
print("=".center(20,"="))
cafe(아메=2000)


menu = {"아메리카노":3000,"마카롱":2000,"핫초코":3000}
cafe(**menu) #이것도 인자의 수를 몰라 *을 사용
'''

def addthree(num):
    return num + 3
print(addthree(100))

print((lambda num:num + 3)(100))
print((lambda num : num * 10)(293))
print((lambda num , num2: num * num2)(100,200))         