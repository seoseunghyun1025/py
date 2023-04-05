'''
# if
h = 9
if h < 12 :
    #h가 12보다 작을 때
    print("오전",h,"가 12보다 작다.")
else :
    #실행문2
    #h가 12보다 크다.
    print("오후",h,"는 12보다 크다.")
'''
'''
h = 12
if h < 12 :
    print("오전",h,"가 12보다 작다")#h가 12보다 작을 때
elif h<13:
    print("점심 먹을래?")
elif h < 18 : 
    print("오후",h,"가 12보다 크고 18보다 작아요") #h가 12보다 클 때
else :
    print("저녁",h, "는 18보다 크다")
'''
'''
bab = input("밥먹을래?")
if bab == "y" :
    bab = input("학식먹을래?")
    if bab == "y" : 
        print("8호관 3층으로 가시오.")
    else :
        bab = input("subway먹을래?")
        if bab == "y" :
            print("8호관 1층으로 가시오")   
        else :
            print("점심먹지마")  
else :
    print("먹지마") 
'''
'''
# for, while
for i in 1,2,3,4,5,6 :
    print("i:",i)

for i in range(0,20,1) : #range(20)과 같다 인덱스는 [0,1,2,...,19]
    print("i:", i)
print("------------")
for i in range(0,20,2) : # 0~19까지 +2씩 출력(짝수 출력)
    print("i:", i)

for i in range(1,20,3) : # 1~19까지 +3씩 출력
    print("i:", i)

# 1부터 10까지 합을 구하시오.
# 2가지 방법으로 range도 쓰고, 명시도 하고


# 첫 번째
sum = 0
for i in 1,2,3,4,5,6,7,8,9,10:
    sum += i 
print(sum)

# 두 번째
sum = 0
for i in range(1,11,1) : 
    sum += i
else :
    print("else안의 문구")
    print(sum)
print("else밖의 문구")
'''
# print(i, end=' ')
n = 0
while n < 11 :
    # print("n:", n)
    # 1 2 3 4로 하고 싶으면
    print(n, end=" ") # end=" "는 공백 수
    n += 1

#sum, 0-10까지 숫자를 더함
n = 0
sum = 0
while n < 11 :
    sum += n
    print(n,"번째 :",sum)
    n += 1
print("총:",sum)

while False:
    print("실행이 되지 않음") # 컴퓨터가 인식하고 흐릿하게 나옴
print("While False 다음 줄")
while True:
    print("무한 루프")
    break

while 0:
    print("실행이 되지 않음")
print("while 0 다음 줄입니다.")