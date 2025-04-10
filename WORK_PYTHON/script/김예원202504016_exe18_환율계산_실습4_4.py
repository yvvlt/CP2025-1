aome = float(input("환전할 단어 금액 입력 : "))

USD = 1458.80
EUR = 1600.67
CNY = 198.03
JPY = 9.92

aome_KRW = aome * USD
aome_EUR = aome_KRW/EUR
aome_CNY = aome_KRW/CNY
aome_JPY = aome_KRW/JPY

print()
print(f"{aome:.2f}달러의 환율 계산 금액은 다음과 같다.")
print(f"원화 : {aome_KRW:.2f}")
print(f"유로 : {aome_EUR:.2f}")
print(f"위안 : {aome_CNY:.2f}")
print(f"엔화 : {aome_JPY:.2f}")
