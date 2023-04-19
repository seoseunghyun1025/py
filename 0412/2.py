lst = ['햄버거','감자튀김','탕수육','라볶이','김밥']
#pop은 리스트 안에 인덱스 값을 없앰 remove도 마찬가지지만, pop처럼 출력 하지는 않음
'''print("lst.pop():",lst.pop()) # 가장 나중에 넣었던 문자열이 나옴
print(lst)
print("lst.pop():",lst.pop()) # 나왔던 문자열은 제외하고 그 다음 문자열이 나옴
print(lst)
print("lst.pop():",lst.pop(0)) # 앞에 문자를 pop함
print(lst)'''
'''
dessert = ["케잌","커피","우유","와플"]
print(dessert)
lst.extend(dessert)
print(lst)
lst.append("케잌")
print(lst)
'''
'''
l1 = ['orange','apple','mango','kiwi','banana']
print(l1)
print(sorted(l1)) # 값이 안 바뀜
print(l1)
l1.sort() # 역순으로 하려면
print(l1) #값을 아예 바꿈 
l1.reverse()
print(l1) #del은 튜플 삭제
l1.clear() #값 클리어
print(l1)
'''
'''
#리스트 컴프리핸션, 리스트를 짧고 빠르게 할 때 사용
l2 = [0,1,2,3,4,5,6,7,8,9,10]
print("l2:",l2)
# 1) for문으로 append
l3 = []
for i in range(11) : # 0~10
    l3.append(i)
print("l3:",l3)
# 2) 리스트 컴프리핸션
l4 = [i for i in range(11)]
print("l4:",l4)
'''

l5 = [i ** 2 for i in range(11)]
print(l5)
# l6 = [i * 3 for i in range(11)]
l6 = [i for i in range(0,31,3)]
print(l6)
l7 = ['hello' for i in range(10)]
print(l7)