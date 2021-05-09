x = 3

# 1)
if x > 2:
    print("Hello", "\n")     # x가 2보다 크면 Hello 출력
    
# 2)
if x > 5:
    print("Hello", "\n")     # x가 5보다 크면  Hello 출력하고
else:                        # 그게 아니면
    print("Hi","\n")         # Hi를 출력해라

# 3)
if x > 5:
    print("Hello", "\n")     # x가 5보다 큰지 보고
elif x == 3:                 # x가 3인지 보고    else if
    print("Bye", "\n")
else:                        # 그게 아니면
    print("Hi", "\n")        # Hi 출력
