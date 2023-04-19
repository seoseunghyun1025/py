#print("python " + " happy")
#print("python\n" * 4)
#print('python' + "언어" + 3*"방가")
#print('#hi')
#print('''hi''')
#print("""hi""")
#print(0)
# #print(03)
# print(0000000003.14)
# print(3.1415 * 100)
#print(5/3)
#print(5/3)
#print(_)

'''
#프로젝트1
num1 = float(input("첫 번째 수 입력 >> "))
num2 = float(input("두 번째 수 입력 >> "))
print("합:",num1 + num2 )
print("차:",num1 - num2)
print("곱:",num1 * num2)
print("나누기:",num1 / num2)

연산식 = input("연산식 문자열로 입력")
연산식 = eval(연산식)
print(연산식)
'''
# x, y = 10, 5
# print(x,y)
# x = y + 1
# print(x,y)
# x /= 2
# print(x,y)
# y += 2
# print(x,y)
# x //= y - 1
# print(x,y)
# print(x + 1, y-1)
# print(x,y)
# y %=y // 2
# print(x,y)
# str = '34'
# print('결과값',int(str))
# m = input()
# print(m + 1)
# distance = 149600
# ex = 1000
# mile = int(input("차의 속도를 입력:"))
# print(mile / 1.61)
# 둘레 = 40120
# 지구 = 2 * 3.141592 * 6378.1
# print("알려진 지구의 둘레: ",둘레)
# print("지구와 같은 원둘레: ", 지구)
# print("차이:",둘레 - 지구)
# ne = int(input("네 자릿수 정수 입력"))
# for i in 1,2,3,4 :
#     na = ne % 10
#     ne //= 10
#     print(na)
# print(len('ab\td'))
# print((10000 <= 9000 < 20000)) 
# print(len('파이썬'))
# print('python 언어'[7])
# print('자바'*3)
'''
str = '어떤 일에든 명확한 - 바람직하며 유일한 - 방법이 존재한다.'
print(str)
slen = len(str)
print(slen)
print(str[str.find('바람직하며'):str.find('유일한')+3])
print(str.replace(' ',''))
'''
'''
a = input("문자열 입력>>")
print("참조할 첨자:",0,"~",len(a)-1)
b = int(input("참조할 첨자 입력>> "))
print("문자열:",b,", 길이:",len(a))
print("참조 문자:", a[b])
'''
'''
a = input("다섯 문자 이상의 문자열 입력>>")
print("입력문자열",a)
print("첫 문자:", a[0])
print("마지막 문자:", a[len(a)-1])
print("첫 문자를 제외한 부분 문자열:",a[1:len(a)])
print("마지막 문자를 제외한 부분 문자열:",a[:len(a)-1])
print("맨 앞과 뒤의 두 문자씩을 제외한 부분 문자열:", a[2:len(a)-2])
print("문자 하나씩을 건너뛴 부분 문자열:",a[::2])
print("역 문자열:", a[::-1])
'''
'''
chur = 'Beautiful is better than ugly.'
print(chur)
print("위 철학을 메소드 replace()를 사용해 다음 철학으로 다시 저장")
chur = chur.replace('Beautiful','Explicit')
chur = chur.replace('ugly','implicit')
print(chur)
'''
'''
url = 'https://docs.python.org/3/tutorial'
print(url[url.find('https'):url.find(':')])
print(url[url.find('docs'):url.find('g')+1])
print(url[url.find('tutorial'):len(url)])
'''
'''
for i in 1,2,3,4,5 :
    print(i)

time = input("시분초 콜론 구분 지어 입력 ")
hours,mins,secs = time.split(":")
print("입력 시간:",hours,mins,secs)
print("{}시 {}분 {}초".format(hours,mins,secs))
folat = float(input("실수 두 개 입력:"))
folat1,folat2 = folat.split(",")
print("{} > {} 결과: {}".format(folat1,folat2,(folat1 > folat2)))
'''
'''
for i in range(3) :
    coffee = input("주문하세요! >> [아메리카노][카페라떼][카푸치노]>>")
    if coffee == "아메리카노" :
        print("%s 주문" % coffee)
    elif coffee == "카페라떼":
        print("%s 주문" % coffee)
    elif coffee == "카푸치노":
        print("%s 주문" % coffee)
    else :
        print("잘모르겠어요..")
else:
    print("주문을 마치겠습니다.")
'''
'''
n = input('찾고 싶은 수 0 ~ 9')
for i in range(0, 100):
    i = str(i)
    if n in i : 
        print(i) 
'''
'''
cnt = 0
more = True
while more:
    height = float(input("키는?"))
    if height < 130:
        cnt += 1
        print("들어가세요","%d명" % cnt)
    else :
        print("죄송합니다. 키가 큽니다.")
    if cnt == 4:
        print("정원이 찼습니다 놀이기구 시작~")
        more = False
else:
    print("놀이기구 끝~")

'''

# more = True
# while more:
#     menu = int(input('''버거, 콤보 번호로 주문하세요!
#                 0. 주문종료
#                 1. 올인원팩
#                 2. 투게더팩
#                 3. 트리오팩
#                 4. 패밀리팩'''))
#     if menu == 0:
#         more = False
#         print("주문을 마치겠습니다.".center(20,"*"))
#     elif menu == 1:
#         print("올인원팩 주문하셨습니다!")
#         print("")
#     elif menu == 2:
#         print("투게더팩")
#         print("")
#     elif menu == 3:
#         print("트리오팩")
#         print("")
#     elif menu == 4:
#         print("패밀리팩")
#         print("")
#     else :
#         print("잘 못 누르셨습니다..다시 눌러주세요")
# else:
#     print("맛있게 드세요!")
'''
answer = 10,20,30,40,29,32
print("당첨 번호!".center(30,'*'))
print(answer)
import random  #from random import randint라고 적으면 random.randint()에서 randint()만 적을 수 있다
cnt = 0
print("랜덤 복권!!".center(30,"="))
for i in range(6):
    n = random.randint(1,45)
    if n in answer :
        print(n,"O", end=' ')
        cnt += 1
    else :
        print(n,"X",end=" ")
else :
    print()
    print("%d개 맞음" % cnt)

days = ['Monday','Tuesday','Wednesday']

while True:
    print("월요일은?")
    day = input("입력")
    if days[0] == day:
        print("정답입니다~")
        print("화요일은?")
        day = print("")

from random import randint
rand = randint(1,10)
print("1~10까지의 난수입니다!!".center(10,"*"))
more = True
while more:
    ans = int(input("맞춰보세요!!>>"))
    if rand == ans:
        print("%d 정답입니다!!" % ans)
        more = False
    elif ans > rand :
        print("%d보다 작은 수!" % ans)
        continue
    else :
        print("%d보다 큰 수" % ans)
        continue
else: # while문 else는 조건문이 변수로 되어있어야 한다 boolean으로는 else문을 작성할 수 없다.
    print("종료합니다!!".center(10,"="))
'''

# print("coffee menu!")
# n = '''1. 카페라떼 2000
#        2. 카푸치노 2500
#        3. 아메리카노 3000
#        4. 카라멜마키아또 4000
#        0. 주문종료'''
# count = 0
# price = 0
# while True:
#     num = int(input(n))
#     if num == 0:
#         print("주문 종류".center(
# 0,"*"))
#         print("총 주문 가격:",price, "원")
#         print(" 안녕! ".center(20,"="))
#         break
#     elif num == 1:
#         count = int(input("수량>>"))
#         price += 2000 * count
#         print("%s %d개 주문하셨습니다" % (num,count))
#         print("총 가격: {}".format(price))
#     elif num == 2:
#         count = int(input("수량>>"))
#         price += count * 2500
#         print("%s %d개 주문하셨습니다.")
#         print("총 가격: {}".format(price))
#     elif num == 3:
#         count = int(input("수량>>"))
#         price += count * 3000
#         print("%s %d개 주문하셨습니다.")`
#         print("총 가격: {}".format(price))
#     elif num == 4:
#         count = int(input("수량>>"))
#         price += count * 4000
#         print("%s %d개 주문하셨습니다.")
#         print("총 가격: {}".format(price))
#     else :
#         print("잘못 누르셨습니다;;")
# cnt = 0
# date = int(input("한 달 최대 일수 입력>>"))
# day = int(input("시작일->0:일, 1:월, 2:화,...,6:토 입력>>"))
# day %= 7
# print("\n", end=" ")
# for i in '일월화수목금토' :
#     print("%s" % i, end=" ")
# else:
#     print()
# if day != 0:
#     print("   " * day, end =" ")
#     cnt += day

# for i in range(1,date + 1):
#     print("%2d" % i, end=" ")
#     cnt += 1
#     if cnt % 7 == 0 :
#         print()
# else: 
#     print()
'''
for i in range(1,6) :
    if i  % 2 == 0:
        s = '*'
    else :
        s = "#"
    print(s * (i-1))

num = 1
while num <= 16:
    num += 3
    if num % 4 == 0:
        continue
    print(num)
print()

for word in 'rain','sun','exit','weather':
    if word == 'exit':
        continue
    print(word)
print()
'''

# num = int(input())
# for n in range(2,num) :
#     for x in range(2,n):
#         if n % x == 0:
#             print('%d * %d = %d' % (x, n//x, n))
#             break
#     else:
#         print(n, '소수(prime number)')

# if 'py' >= 'pi':
#     print("py가 더 크네요")
# while True:
#     reply = input("종료 stop or quit>>")
#     if reply == 'stop' or reply == 'quit':
#         print(reply)
#         print("종료".center(20,"*"))
#         break
lst = [1,5]
lst[0] = 3
lst.append(7)
lst[1:3] = [10]
print(lst)