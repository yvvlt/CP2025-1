pp = 1500
np = 2500
ep = 800
p = int(input("연필 판매 수량 입력 : "))
n = int(input("노트 판매 수량 입력 : "))
e = int(input("지우개 판매 수량 입력 : "))

pt = pp*p
nt = np*n
et = ep*e
t = pt + nt + et

print()
print(f"{p}자루 연필의 판매 금액 : {pt}원")
print(f"{n}권 노트의 판매 금액 : {nt}원")
print(f"{e}개 지우개의 판매 금액 : {et}원")
print(f"총 판매금액 : {t}원")
