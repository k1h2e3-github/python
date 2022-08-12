import random
foodlist = ['짜장면', '짬뽕', '우동', '돈까스']
random.shuffle(foodlist)
#음식 리스트 출력
for i in range(1, len(foodlist)+1):
    print("{}. {}".format(i, foodlist[i-1]))
 #먹고 싶은 메뉴 받기
y = input()
if y not in foodlist: #먹고 싶은 메뉴 없으면
    new_list = []  
    for j in range(3):# 새로운 매뉴판 생성
        x = input()
        new_list.append(x)
#그중에서 1개 출력
def prt(new_list):
    return random.choice(new_list)
    
print(prt(new_list))
