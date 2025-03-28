# 반복문을 사용해서 1-10 출력 
for i in range(1,11)
    print(i)

a = 10 
if a>5 and a<9: # True and False # 앞에가 펄스면 계산안하고 그냥 넘어감. 조금이라도 속도를 빠르게 하기 위한 로직 
    print(a)

if a>5 or a<9: # True or False 
    print(a)

# 90 \t 탭으로 많이 씀 
#92 역슬래쉬 줄을 바꿔 출력하지 않겠다 
#95 문자 선택 연산자 

a_list = [1,2,3,4,5]
print(a_list[2]) #/ 중요 
print(a_list[1:4]) # 시작위치:끝나는위치-1 - 슬라이싱 자르다?는 느낌 #2,3,4 / 중요 
print(a_list[:3]) # [:끝나는위치-1] - 처음부터 시작해라 #1, 2, 3
print(a_list{2:]) #[시작위치:] -끝까지 출력 3,4,5
print(a_list[::2]) # 2개씩 증가해서 출력 1,3,5
print(a_list[::3]) # 1,4
print(a_list[::-1]) # 역순으로 출력해라 5,4,3,2,1
print(a_list[:-1]) # 1,2,3,4 / 중요 
print(a_list[::-1]) # /중요 

a = "안녕하세요" #하나씩 번째 출력 가능하다 / 리스트와 같다? 
print(a[2])

a = "안녕하세요" #이 한글 문자도 리스트랑 똑같음 
print(a[2])
print(a[1:4])
print(a[:3])
print(a[2:])
print(a[::-1])
print(a[:-1])

print(a[:7]) #슬라이싱은 에러가 안나지만, 슬라이싱은 없는 값 출력시 에러가 나지 않음. 
print(a[7]) # 인덱싱 없는 것 출력시, 에러 Index Error 

print(len(a_list)) #리스트 개수 확인 
print(a_list[:len(a_list)-1])
print(len(a)) #문자열 길이 

# a_list[1:11:2]
for i in range(1,11,2): 
    print(i,end=".") #줄바꿈 없이 출력 #end를 안넣으면 한줄이 아닌 줄바꿔서 출력됨 

sum = 0 
i = 0 
for i in range(1,100+1):
    sum = sum + i 
    print("sum : {}".format(sum))
    if sum>=100: break 
#for 문을 멈추는 법, break

print("1-100까지 합계 : {}".format(sum)) # 이정도는 외우면 좋을 거 같음 500500
print("sum이 100넘었을때 1값 : ",i)
print("합계가 100이 넘었을 때 sum값 : ", sum)



# 합계가 100 넘는 위치의 숫자는 얼마일까요? 1+2+3+4+5+6+7..... 합계가 100넘는 위치 어디인지 출력하시오. 그 때 값도 출력하시오. 
