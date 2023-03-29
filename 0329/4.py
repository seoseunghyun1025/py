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