# 무한루프 "exit"면 프로그램 종료 "apple"이면 다시 단어 입력 다른 입력들은 3글자 출력 후 루프
'''
while True:
    word = input("단어를 입력하시오 ")
    if word == "exit":
        print("넌 exit를 입력했다. break를 만난다. ")
        break
    elif word == "apple" :
        print("넌 apple을 입력했다. 다시 입력해! ")
        continue
    else:
        for i in range(3):
            print(word)
        else:
            print("해당 단어 끝 ")
    print("apple을 넣으면 절대 볼 수 없음 ")

# import random
# print(random.randint(0,10000))

from random import randint
print(randint(0,10000))
'''
# 놀이동산 탑승 
# 총 정원 4명
# 조건 키 150이상만 
# 사람들한테 키를 물어보고, 탑승
# 150이상 4명이 되면 놀이기구를 시작
while True:
    정원 = int(input("정원이 몇 명입니까"))
    if 정원 >= 5:
        print("정원이 많습니다.")
        continue
    elif 정원 < 4: 
        print("정원이 부족합니다.")
        continue

    키 = int(input("키는 몇 입니까?"))
    if 키 >= 150 :
        print("놀이기구 시작")
        break
    elif 키 < 150 :
        print("키 150이상만 가능합니다..")
        