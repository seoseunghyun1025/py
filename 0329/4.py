'''
print("hello \n world") # 엔터
print("hello \t world") # 여러 칸 띄기
print("hello\bworld") # \b 앞 한 단어 없어짐
print("hello\vworld") #
'''
str_a = "하하하"
#str_b = "호호호"
print(type(str_a))
print(str_a.replace("하","호"))
print(str_a) #값이 바뀌지 않음
str_b = str_a.replace("하","호")
print(str_b) #값을 넣었기 때문에 값이 바뀜

str_c = "안녕하세요. 파이썬 수업입니다. 파이썬, 파이썬,파이썬, 파이썬,파이썬, 파이썬,파이썬, 파이썬,파이썬, 파이썬"

print(str_c.replace("파이썬","자바", 5)) #첫 인자(파이썬)를 자바라는 두 번째 인자로 바꾸는데 5개까지만 바꾸는 명령어

# 입력: 6자리 실수를 입력받는다. 222.788
# 출력: 실수인 각 자리의 합을 출력한다. 2+2+2+7+8 =>
# input(), int(), str.replace()

num = input("6자리 실수를 입력하시오.") # 212.222
num = num.replace(".","") #212222
print("sum: " , int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]) + int(num[5]))
sum = 0
for a in range(6) :
    sum += int(num[a]) 
print(sum)