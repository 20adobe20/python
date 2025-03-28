# 파이썬 타입 
# bool타입, 숫자 - int 타입, float 타입, str 타입

# bool 타입 - True, False 
# bool 타입 - 정수형 타입 소수점 없음. 
# float타입 - 실수형 타입 : 소수점 있음 
# str타입 - answkduf xkdlq : "",''안에 입력을 해야 함 . 
# if TrueL:
#       print("거짓입니다.")


print(1+2)

print(1+1.2)

# print ("안녕+1") #타입이 다른 경우 error 
print("안녕" ,1)

print(10/3)
print("숫자 : {:.2f}"/format(10/3))

# 컨트롤 k c 

print
; 숫자는 큰 따옴 표 
\" \"

s string 정수
d digit 
"출력값, ", 100
f float 소수점? c char 

\n 한줄 줄바꿈 

부동소수점 %.2f 둘째자리까지 만 읽을래요 

;변수 
# 특수문자 x 숫자시작 x 공백올수없음 , 대소문자 구분, 예약어 사용 불가능 , 한글 사용가능하지만 사용하지 않은는 것이 좋다. 변수명은 의미를 알 수 있게하는 게 좋음 

#트루문은 들여쓰기를 해야 실행이 됨. 

if true: 
    print("거짓입니다.")

if 10>3: #True
    print("정상")

if True: 
    print("정상")

eles: 
    Print("정상") 

print(1+2)
print(1+1.2)
print("안녕"+1)
print(10/3) 




# 타입변경 문자열 ▶ 숫자형태일 경우 (문자가 들어가 있으면 안됨) 

# print(int("안녕")) # 숫자형태 문자열만 숫자타입으로 변경가능 
print(int("1"+1) 
      
#숫자를 타입 변경 - int타입, float 타입으로 변경 가능 
print(int(1.5)) #실수형 -> 정수형으로 타입변경 : 소수점이 사라짐. 
# 문자열 float타입을 int타입으로 변경은 안됨. 
# print(int("1.5")) # error
print(floast("1.5")) # 가능 

print(str(1.5)) # 숫자는 문자열로 언제든 만들 수 있다?  / 문자열 타입 변경 

#-------------------
# 변수 
a = 10 # = 할당의미 # int 타입 정수
a = 5  # 10을 지우고 5를 넣어줘 
b = 1.5 # float타입 
c = "안녕" #str타입 / 한글이니까 

print(c+a) #타입이 다르기 때문에 에러 / str 타입 + nt 타입 더하기 연산은 불가능 

print(a+b) #int타입 + float 타입 더하기 가능 (숫자)

# list 타입 - 값을 여러개 저장 
list_a = [1,2,3,4]
print(list_a) # 다 나옴 
print(list_a[0]+list_a[1]+list_a[2]+list_a[3]) # 0번방 1번방 2번방 3번방 0x11 이것이 여기다가 저장이 됨. 우리눈엔 1,2,3,4로 보이지만 실제론 이런 로직으로 이루어져있음 #변수 하나 쓰는거보다 리스트 엄청 많이 씀 / 요즘은 데이터 전송해야할 게 1억개 만개 이러니까 변수를 만개 선택할 수 없고 언제 다 만개를 선언하고 있음 리스트로 한번에 쭈욱 해서 많이 쓴다 

# input() : 데이터를 입력받는 명령어 - str타입 1개 / 무조건 스트링 타입 한개로 나옴 문자, 숫자 무얼넣어도 
score = input("데이터를 입력하세요.>>")
print("입력 데이터 : ",score)

## 두수를 입력받아 합계, 평균을 출력하시오. 
num1 = input("숫자를 입력하세요.>>")
num2 = input("숫자를 입력하세요.>>")
print(num1+num2) #100200 > 두수가 더해지는 게 아니라 문자열로 나옴 스트링이라 

# 문자열타입 -> int 타입으로 변경 
num1 = int(input("숫자를 입력하세요.>>"))
num2 = int(input("숫자를 입력하세요.>>"))
print(num1+num2) #300 > int 값이 라 합쳐짐  

# 숫자 에러나는 은행을 보면 신용이 안가니 중요하다 

score = int(input("점수를 입력하세요.>>"))
if score>=60: 
    print("합격")
elso: 
    print("불합격")
    

score = int(input("점수를 입력하세요.>>"))
if score>=70:
    print('합격')
elif score>=60: #elif
    print("재시험") 
else:
    print("불합격")

score = int(input("점수를 입력하세요.>> "))
# 90점 이상 a,b,c,d,f 출력하시오. 
if score>=90: print("A")
elif score>=80 print("B")
elif score>=70 print("C")
elif score>=60 print("d")
else: ("f")
