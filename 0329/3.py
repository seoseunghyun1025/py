'''
a = "python"
#방법1
print(a[0], " ", a[1], "..." , a[5])
#방법2
print("python"[0], "... ", "python"[1], " ...", "python"[5])
print("동양미래대학교"[0])
#문자열 안에 []를 넣으면 안됨
print("동양미래대학교[0]")
#length 안에 있는 값을 해야함 오바해서 적으면 오류남
print(len(a)) #7글자임
'''
#중간때 문제 나옴!!


'''
school = "동양미래대학교"
print("school[:]",school[:]) #동양미래대
print("school[:]", school[0:3]) #동양미
print("school[1:4]",school[1:4]) #양미래
print("school[2:4]",school[2:4]) #미래
print("school[1:]",school[1:]) #양미래대
print("school[0:len(school)]", school[0:len(school)]) #동양미래대
'''

school = "동양미래대학교-컴퓨터소프트웨어공학과"
print("school[:]",school[::-1]) #과학공어웨트프소터퓨컴-교학대래미양동(음수면 거꾸로 출력)
print("school[:]",school[::]) #동양미래대학교-컴퓨터소프트웨어공학과
print("school[:len(school):2]", school[0:len(school):2]) #동미대교컴터프웨공과
print("school[1:4]",school[8:len(school):2]) #컴터프웨공과
print("school[2:4]",school[8:len(school)]) #컴퓨터소프트웨어공학과
print("school[1:]",school[0:15:4]) #동양미래대학교-컴퓨터소프트웨어 -> 동대컴프