lst = [] #리스트 생성
print(type(lst))
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
lst.append("탕수육")


lst.append("파스타")
lst.insert(0, "학식")
lst.insert(0,"subway")
lst.append("탕수육")
lst.append("탕수육")
lst.append("탕수육")
print(lst)
print("list에서 3번째에 있는 값: ",lst[2])
for i in range(len(lst)) :
    print(i,"번째에 있는 값:",lst[i])
else :
    print("끝")

for i in lst :
    print(i)
else :
    print("끝")
print('lst.count("탕수육)', lst.count('탕수육'),'lst.index("탕수육")', lst.index("탕수육"))

print(lst[0:len(lst):1]) #0~(len(lst)-1)까지 한 칸씩
print(lst[0:8:2])
lst.remove("김밥")
print(lst)
# if문 활용
item = '커피'
if item in lst:
    print("커피 존재함", lst)
else :
    print("커피 존재 안 함", lst)
