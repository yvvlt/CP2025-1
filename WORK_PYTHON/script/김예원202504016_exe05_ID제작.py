ni = input("영문이름의 이니셜 입력 : ")
bd = input("생년월일 입력(yymmdd) : ")

ID = ni + "&" + bd[1] + bd[0] + bd[-1] + bd[3]

print()
print("사용자 ID :",ID)
