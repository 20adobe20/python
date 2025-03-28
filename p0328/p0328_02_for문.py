print("안녕하세요")
print("안녕하세요")
print("안녕하세요")

# range(3) -> 0,1,2 ; 0부터 시작임 기억하삼 
for i in range(3): #3번을 반복해줘 
    print("안녕하세요.")

# range(1,4): ->1,2,3 : 4 앞까지 출력 
for i in range(1,4): 
    print("안녕하세요." ,1)

#이게 햇깔릴까봐 아래처럼 하기도 함 
for i in range(1,3+1): 
    print("안녕하세요." ,1)

# range(1,11,5) - 첫번째숫자:시작번호, 두번째숫자:마지막번호 -1만큼, 세번째 숫자: 간격 / 몇 번째 간격으로 출력을 할래 
for i in range(1,12,2) #1부터 12까지인데 2씩 증가하면서 해라 
    print("안녕" ,i)

#range() 자리에 list 타입 가능 
a_list = [1,2,3,4,5]
for i in a_list
    print("안녕",i)
