'''
def addthree(num):
    return num + 3
     
print(list(map(addthree,[10,20,30,40,50])))
print(list(map(lambda x : x + 3,[10,20,30,40,50])))

def gop(num):
    return num * 5 + 10

lst = [1,2,3,4,5,6]
print("=".center(20, "="))
print(list(map(gop,lst)))
print(list(map(lambda x : x * 5 + 10,lst)))

def sum(num,num2):
    return num + num2

lst2 = [10,20,30,40,50]
lst3 = [1,2,3,4,5]
print("=".center(20,"="))
print(list(map(sum,lst2,lst3)))
print(list(map(lambda x,x1 : x+x1,lst2,lst3)))
'''
def positive(x):
    if x > 0:
        return True
    else:
        return False
def positive2(x):
    return x>0
print(list(filter(positive, [10,-2,3,-5,9])))
print(list(filter(positive2, [10,-2,3,-5,9])))