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
for i in 1,2,3,4,5 :
    print(i)