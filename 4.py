print("안녕 " + "잘지내니?")
print("너 혹시 몇 살이니?" + 19)              # 형식에러 : 문자형만 문자형에 연결할 수 있음. "문자열과 숫자형은 연결할 수 없음."
print("너 혹시 몇 살이니?" + str(19)+"살이야") # 정수 19를 문자형으로 변환해준다.


x = 19             # 숫자
y = "19"           # 문자
print(srt(x) + y)  # x를 문자형으로 변환해 문자열로 합쳐서 출력한다. 캐스팅한다.
print(x + int(y))  # 문자형인 y를 숫자형으로 변환해서 사칙연산(+)으로 합의 값을 출력한다.
