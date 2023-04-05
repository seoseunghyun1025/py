# 무한루프 "exit"면 프로그램 종료 "apple"이면 다시 단어 입력 다른 입력들은 3글자 출력 후 루프
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