#str = "파이썬수업 씨수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업"
#str2 = "파이썬수업, 씨수업, 자바수업, 이썬 수업, 파이썬수업"
'''
#replace
print(str.replace("파이썬", "자바",3)) #앞 3개만 자바로 바꿔줘

#count 몇 개인지 세는 명령어
print(str.count("파이썬")) # 파이썬이 몇 개가 들어있는지 카운트

#find, index
print(str.find("파이썬")) # 찾고자 하는 파이썬이 몇 번째에 있는지 찾아줌(앞 단어부터 찾음)
print(str.index("파이썬")) 

#print("find ",str.find("에이"), " index " , str.index("에이")) # 위치를 알려주는데 index는 오류를 출력, find는 -1을 리턴

#split
print(str.split())
print(str.split(",")) #,로 구분하여 출력
print(str2.split("업")) #업으로 구분하여 출력
'''
'''
#join
print("**".join(str2)) #문자 사이 사이를 **로 구분하여 출력

#format
print("3+4=", 3+4)
f1 = "{} + {} = {}".format(3,4,3+4)
f2 = "{0} + {1} = {2},{2},{2},{2}".format(3,4,3+4) #0은 format의 첫 번째 1은 format의 두 번째 등
f3 = "{0:d} + {1:f} = {2:f},{2:f},{2},{2}".format(3,4.0,3+4.0) #float은 f(소수점 여섯 째 자리까지 출력) 정수는 d로 생략 가능(생략하면 소수점 첫 번째만 나옴)
f4 = "{0:10d} + {1:10f} = {2:10.3f}".format(3,4.0,3+4.0) #10칸 만큼 공백, .3f는 소수점 세 번째 자리까지 출력

print(f1)
print(f2)
print(f3)
print(f4)
'''

#boolean
'''
print(type(True),type(False))
a = "hello"
print(bool(a),bool("hi"),bool("0"),bool(1.2))
print(bool(""),bool(0)) #빈 문자와 0(정수형)만 false
print(int(True), int(False), str(True)) #str 변수로 하면 큰일남
'''
