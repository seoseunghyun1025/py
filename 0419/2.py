# 여러 리스트들을 zip으로 묶음
'''
l1 = ['한식','중식','일식']
l2 = ['전주식당','전가복','초밥집']
l3 = ['제육','탕수육','연어초밥']
z = zip(l1,l2,l3)
print(type(z))
print(z)
print(list(z))

stu_id = [1,2,3,4,5,6,]
weight = []
height = [111,222,333,444,]
print(type(stu_id))

#dictiocnaryf
#list1 => dictionary x
z1 = zip(l2,l3)
print(dict(z1))
print(list(z1))
z2 = zip(l1,zip(l2,l3))
print(dict(z2))

l4 = ['제육','탕수육','연어덮밥']
print(list(enumerate(l4))) #012로 만드는데 튜플로 만들고 그 위를 리스트 형식으로
print(dict(enumerate(l4))) #이건 마찬가지로 위를 딕셔너리로
'''

# #문제
# subject = ['파이썬','자바','C++','AI','알고리즘']
# classroom = [101,102,103,104,105]

# z1 = dict(zip(subject,classroom))
# a = "과목명을 입력하시오 파이썬, 자바, C++, AI, 알고리즘>>"
# while True:
#     sub = input(a) 
#     if sub == "quit":
#         print("종료")
#         break
#     if sub in  z1:
#         print(z1[sub])
#     else:
#         print("몰라요")
#         continue

from random import choice

rsp = {'가위':'보오','바위':'가위','보오':'바위'}
tit = ['비김','철수','영희','승리']
good = ('가위','바위','보오')

print('*' * 17)
print('{:4} {:4} {:4}'.format(tit[1],tit[2],tit[3]))
print('*' * 17)

ccnt = 0
ycnt = 0
bcnt = 0
for i in range(20):
    cs = choice(good)
    yh = choice(good)
    if cs == yh:
        bcnt += 1
        print("{:4} {:4} {:4} {}".format(cs,yh,tit[0],bcnt))
    if rsp[cs] == yh:
        ccnt += 1
        print("{:4} {:4} {:4} {}".format(cs,yh,tit[1],ccnt))
    else:
        ycnt += 1
        print("{:4} {:4} {:4} {}".format(cs,yh,tit[2],ycnt))
else :
    print("총 게임 회수: {} 비긴 횟수: {}".format(20,bcnt))
    print("철수 승률: {}".format((ccnt + bcnt * 0.5)/20))
    print("영희 승률: {}".format((ycnt + bcnt * 0.5)/20))    