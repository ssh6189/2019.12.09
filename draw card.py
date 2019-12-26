import random
import os

coin = 1


while coin == 1:

    str(input())
    os.system('cls')

    print("카드를 뽑으시려면 1을, 그만두시려면, 아무버튼이나 입력하시오.")
    coin = int(input())

    if coin == 1:

        a = random.randrange(1, 13)
        b = ["하트", "스페이드", "클로버", "다이아몬드"]
        c = random.choice(b)
    
        
        class card:
            ac = a
            bc = c

        cw = card()
    
        print(cw.bc, cw.ac)
        

    else:
        break

    
