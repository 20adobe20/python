# 구구단 출력하시오 
# 2 x 1 = 2 
# 9 x 1 = 0 

# for i in range(2,10): 
#    # print("[ {} 단 ]".format(i))
#     for j in range(1,10):
#         print("{} x {} = {}".format(1,j,1*j),end="")
#     print()

# ## 은행가면 001 002 003... 010 011 012... 999 
# for i in range(0, 1000):
#     print("{:03d}".format(i))

# 기억이 안나도 계속 입력해보라 


for i in range(1,10): 
    # print("[ {} 단 ]".format(i))
     for j in range(2,10):
         print("{} x {} = {}".format(j,i,1*j),end="")
     print()

# 이 정도까지는 대충 알고 있어야함 
