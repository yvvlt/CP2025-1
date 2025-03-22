fv = int(input("첫 번째 수 입력 : "))
op = input("연산자 선택(+, -, *, /, ^) : ")
sv = int(input("두 번째 수 입력 : "))

if op == '+':
    print(fv,"+",sv,"=",fv+sv)
    
elif op == '-':
    print(fv,"-",sv,"=",fv-sv)
    
elif op == '*':
    print(fv,"x",sv,"=",fv*sv)
    
elif op == '/':
    print(fv,"÷",sv,"=",fv/sv)
    
elif op == '^':
    print(fv,"^",sv,"=",fv**sv)
