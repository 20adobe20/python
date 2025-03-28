fruit = ['사과','배','딸기','바나나','멜론']
         
# enumerate index 번호를 받을 수 있음. 
for i, furit in enumerate(fruit):
    if i != len(fruit): 
        print("{}.{}".format(1+1,fruit), end=",") 
            else:
                print("{}.{}".format(i+1,fruit),ends="")
# 맨 마지막이 숫자이면 쉼표 붙이고 숫자가 아니면쉼표 붙이지ㄴ


# score = [65,60,100,100,50]

# for score in scores:
#     print(score,end="")