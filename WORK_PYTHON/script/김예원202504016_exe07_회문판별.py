st = input("문자열 입력 : ")
std = st.strip()
std = std.replace(' ','')

if std == std[::-1] :
    print("입력한 데이터 \'%s\'는(은) 회문입니다."%st)
else :
    print("입력한 데이터 \'%s\'는(은) 회문이 아닙니다."%st)
