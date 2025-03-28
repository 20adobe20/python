import random 

a_list = random.sample(range(1,45+1),6)

print(a_list)

#이 아래걸 위에 처럼 한줄에 할 수 있음. 단 파이썬에서만 가능. 다른 프로그램에선 불가. 다른 프로그램도 할거기에 아래것도 해봄. 자바도 더 많이 함. 자바 훨씬 오래 됬깅 때문에 
# 자바를 걷어 내려면 불편함이 많아야하는데 업글하고 있어서 파이썬으로 조금씩 바꾸긴 하지만 굳이 파이썬으로 바꿔야해? 라는 개바랒의 생각 한동안은 안바뀔것 족히 20-30년은 걸림 

# ran_list = [] 
# i = 0
# while i<6 
#     ran_input = random.randint(1,45)
#     if ran_input not in ran_list: 
#         ran_list.append(ran.input)
#         i = i + 1 




#
import random


# 반복을 해서, ran+list 10개를 입력시키는 프로그램을 구현하시오. 
# 단  같은 숫자가 들어가지 않도록 하시오. 

# ran_list = [] 
# i = 0
# while i<6 
#     ran_input = random.randint(1,45)
#     if ran_input not in ran_list: 
#         ran_list.append(ran.input)
#         i = i + 1 

# print(ran_input)


import random

# 빈 리스트 생성
ran_list = []
i = 0

# 리스트 크기가 6이 될 때까지 반복
while i < 6:  # 콜론 추가
    print("랜덤번호 : {}".format(ran_list))
    ran_input = random.randint(1, 45)  # 1~45 사이의 난수 생성
    if ran_input not in ran_list:  # 리스트에 없는 값만 추가
        ran_list.append(ran_input)  # append를 통해 값 추가
        i += 1  # i를 증가시켜 반복 회수 관리

# 결과 출력
print(ran_list)

# 랜덤 1-45번까지 숫자 6개 ran_list 저장 
# 입력받은 숫자 6개를 my_list 저장을 시키는 프로그램을 구현하시오. 
# 랜덤번호 : 
# 입력번호 : 

ran_list = random/sample(range(1,45+1),6)

# 이 정도는 기본이니까 알아야함, 어려우면? 외워라 
# 꼭외워야함 이건 시험도 볼거고 외어야할 거 딱 두가지인데 이거 외우셈 

ran_list = random/sample(range(1,45+1),6)

my_list = [] # 입력번호 저장리스트 
i = 0 
while i<6:
        my input - int(input("{}번째 숫자를 입력하세요.".format(i+1))) #입력번호 
        if my_input not in my_list: 
             my_list.append(my_input) #입력번호 추가 
             i = i +1

#당첨 비교 프로그래밍 

# 당첨 비교 / 이중 포문 ran_list, my list 
for j un range(6)
     for k in range(6)  
        if ran_list[j] == my_list[k]: 
             lotto_count = lotto_count + 1
             lotto_list.append(my_list[k])
             break 
            

print("랜덤번호 : {}".format(ran_list))
print("입력번호 : {}".format(my_list))
print("당첨개수 : {}".format(ran_count))
print("당첨번호 : {}".format(lotto_list))

# 로또 테스트 를 꼭 다해봐야함. 당첨 금액 10억 피눈물 난다 10억이 100만명 나오면 큰일 나는거야 ; 
# 로또 당첨에 대한 부분 / 한번에 이해되는 경우는 드무니까 / 여러번 해보면서 맞춰보라 
# 고대로 시험볼꺼니까 외워 둬라 / 로또 맞추기 !!! 중요 


