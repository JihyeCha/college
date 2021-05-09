# 여러 줄 주석 : shift + Alt + A
# 한줄 한줄 : ctrl + /

x = 5       # 변수 x = 정수형 5 선언
y = 3       # 변수 y = 정수형 3 선언
z = 1.2     # 변수 z = 실수형 1.2 선언

print("1)", x+y+z)        # 정수형 x, y와 실수형 z를 더한 값 출력
print("2)", x-y-z)        # 정수형 x, y와 실수형 z를 뺀 값 출력 - print("2)", (x-y)-z)
print("3)", x*y*z, "\n")  # 정수형 x, y, z를 곱한 값에 출력 후 한줄 공백 라인
print("4)", x%y%z)        # x를 y로 나누고 남은 값에서 z를 나눠서 남은 값 출력 - print("4)", (x%y)%z)
print("5)", x**y**z)      # x의 y곱에 z곱 - print("5)", x**(y**z))
print("5)", (x**y)**z)    # x의 y곱하고 z곱
print("6)", x**y)        
