# # 두수를 입력받아, 두수 사이의 합계를 구하시오. 
# # 예 : 1,7 1,2,3,4,5,6,7까지 합을 출력하면 됩니다.

# #1,10 -> 10,1 을 실수로 하면 잘 안나옴. 어케하면 될까? 비교하면 됨. 작은수를 앞으로 큰수를 뒤로 교체하게 해주는 명렁 

# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# print(num1,num2)

# # if문 비교 num1, num2 num2가 더 큰지 확인 
# if num1>num2:
#     t = num1 
#     num1 = num2 
#     num2 = t 
#     #num1,num2 = num2,num1 #위에건 다른 프로그램 다 되는데 이건 파이썬 만됨, 위에건 되도록 알아두기 

# #반복문을 1부터 100까지 넣어보세요 

# sum = 0 
# for i range(num1,num2+1)
#     sum = sum + i 
#     print("i : {}. sum : {}".format(i,sum))

# print("{}에서 {}까지의 합계 : ",format(num1,num2,sum))


# # 구구단 출력 
# for i in range(2,9+1):
#     print("[{}]".format(i))
#     for j in range(1,9+1):
#         print("{} * {} = {}".format(i,j,i*j), end)
#     Print()
    


# # 3,5,7,8단 홀수단만 출력하시오 
# for i in range(3,9+1,2):
#     print("[{}]".format(i))
#     for j in range(1,9+1):
#         print("{} * {} = {}".format(i,j,i*j), end)
#     Print()
    
# # 3,5,7,8단 홀수단만 출력하시오 
# for i in range(2,9+1):
#     #if
#     if i%2 == 1: # 짝수라면 0: 
#         print("[{}]".format(i))
#         for j in range(1,9+1):
#             print("{} * {} = {}".format(i,j,i*j), end)
#         Print()

# 시작단과 끝나는 단을 입력받아, 출력하시오. 
# 2, 6 -> 2~6단까지 출력 

sum = 0 
num1= int(input("nun "))
num2= int(input("nun "))
for i in range(num1,num2+1):
    for j in range(1,9+1): #+1이 없으면 8까지만 감
        print("{} * {} = {}".format(i,j,i*j), end=" ") # end 
    print()



