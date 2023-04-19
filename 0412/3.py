짝수 = [i ** 2 for i in range(0,11,2)]
print(짝수)
짝수2 = [i ** 2 for i in range(11) if i%2==0]
print(짝수2)

###########################################
print("####################################")
짝수면서3의배수 = [i ** 2 for i in range(11) if i%2 == 0 if i % 3 ==0]
print("짝수면서 3의 배수:",짝수면서3의배수)

print("####################################")

#list를 복사
#shallow copy
a = [0,4,16,36,64,100]
b = a # 메모리 주소를 공유 a가 바뀌면 b가 바뀌고 b가 바뀌면 a가 바뀜
print("a:",a)
print("b:",b)
a.pop()
print("after a.pop()")
print("a",a)
print("b",b)
print("a is b:", a is b)
print("##################################")

#deep copy
##c = a[:]
#c = a.copy()
c = list(a)
print("a:", a)
print("b:", b)
print("c:", c)

c.append(1234)
a.pop()
print("a:",a)
print("c:",c)
print("a is c:", a is c)