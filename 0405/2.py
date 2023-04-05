'''
h = 9
if h < 12 :
    #h가 12보다 작을 때
    print("오전",h,"가 12보다 작다.")
else :
    #실행문2
    #h가 12보다 크다.
    print("오후",h,"는 12보다 크다.")
'''
'''
h = 12
if h < 12 :
    print("오전",h,"가 12보다 작다")#h가 12보다 작을 때
elif h<13:
    print("점심 먹을래?")
elif h < 18 : 
    print("오후",h,"가 12보다 크고 18보다 작아요") #h가 12보다 클 때
else :
    print("저녁",h, "는 18보다 크다")
'''
bab = input("밥먹을래?")
if bab == "y" :
    bab = input("학식먹을래?")
    if bab == "y" : 
        print("8호관 3층으로 가시오.")
    else :
        bab = input("subway먹을래?")
        if bab == "y" :
            print("8호관 1층으로 가시오")   
        else :
            print("점심먹지마")  
else :
    print("먹지마") 