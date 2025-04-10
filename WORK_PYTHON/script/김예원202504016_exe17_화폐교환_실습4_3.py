em = int(input("교환할 금액 입력 : "))
count = []
unit = [50000,10000,5000,1000,500,100,50,10]

for x in unit:
    count.append(em//x)
    em %= x

print()
print(f"오만원 : {count[0]}장")
print(f"만원 : {count[1]}장")
print(f"오천원 : {count[2]}장")
print(f"천원 : {count[3]}장")
print(f"오백원 : {count[4]}개")
print(f"백원 : {count[5]}개")
print(f"오십원 : {count[6]}개")
print(f"십원 : {count[7]}개")
