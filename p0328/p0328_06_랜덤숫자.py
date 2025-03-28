# 숫자 맞추기 프로그램 
import random

lotto = random.randint(1,45) 

#---
for i in range(10):

    input_num = int(input({}"숫자를 입력하세요.(1-45번사이)>> ".format(i+1)))


    # 랜덤번호와 입력번호 비교 
    if lotto==input_num:
        print("당첨")
        break # for문 종료 
    elif lotto>input_num:
        print("틀렸습니다. {}보다 더 작은수를 입력하세요!".format(input))
    else:
        print("틀렸습니다. {}보다 더 작은수를 입력하세요!".format(input))


#--

print("랜덤번호 : {}".format(lotto))
print("입력번호 : {}".format(input_list))


# 이 정도는 외웠으면 좋겠습니다 여러분이 
