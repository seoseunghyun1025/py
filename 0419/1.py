#0419
'''
l1 = [1,2,3,4]
t1 = (1,2,3,4)
print(l1)
print(t1)
print(t1.count(2))
'''
# 튜플은 수정 안 됨
'''
t1 = (1,2,3,4)
t1 = list(t1) #수정하려면 t1을 리스트로 만든다
t1.append("아메리카노")
print(t1)
t1 = tuple(t1)
print(t1)

t2 = ()
print(t2)
t3 = 30,20,10,50,40
print(t3)
i4 = 10
print(type(i4))
t4 = 10, #튜플로 만들려면 콤마를 적으면 된다.
print(type(t4))
print(t4)

lst = [10,20,30,40,4,5,6,1,1]
lst.sort()
print(lst)
print("t3:",t3)
print("soted(t3):",sorted(t3))
'''
#for문을 튜플로 사용
'''
t10 = 1,2,3,4,5 #튜플임
for i in t10 :
    print(i)
'''
# dictionary
#d1 = {k1:v1, k2:v2, k3:v3}
'''
student = {}
d2 = dict() #dict(), list(), tuple(), int(),float(),str()
# 사전에 값을 추가하는 것
#1) 추가방법 1
student[101] = '홍'
student[102] = '김'
student[103] = '박'
print(student)
print("student[101]:",student[101])
# 오류남 print("student[0]:",student["gkgk"])
lec = {}
lec['강좌명'] = '파이썬'
lec['개설년도'] = 2023
lec['수강생']= ['홍','김','박','고']
lec['인원']=35
print(lec)
#인원수를 변경하는 방법
#2) 추가방법2
lec['인원'] = 20
print(lec)
lec.update({'인원':10})
print(lec)

lec.update({'강의실':213,'교수':'이희진'}) #키가 존재하지 않는 다면 새로 추가 존재하면 수정
print(lec)
'''
######################################
month = {'a':'1월','b':'2월','c':'3월','d':'4월','e':'5월','f':'6월','g':'7월','h':'8월','i':'9월','j':'10월','k':'11월','l':'12월'}

'''
print(month.keys()) #키 명
print(month.values()) # 키의 데이터
print(month.items()) # 튜플형식으로 키랑 values
print('#3')
# 3
for key in month.keys(): # str이어도 숫자로 나옴
    print(month[key])
print("#######################3333")
for value in month.values(): #print에 value만 적어도 값이 나옴
    print(value)
print("################################`")
for item in month.items() : #print에 item을 적으면 키와 값이 출력(튜플 형식으로)
    print(item)
print("##################################")

for item in month.items() :
    print("key:", item[0])
    print("value:",item[1])
'''
######################################
'''
print(month['a'])
print(month.get('a'))

#dictionary 삭제
print(month)
print("#########################")
print(month.pop('a')) # key를 줘야함 values 출력
print("".center(30,"*"))
print(month.popitem()) # 맨 마지막 것을 삭제함
print("".center(30,"*")) # items를 출력
print(month) 
'''

