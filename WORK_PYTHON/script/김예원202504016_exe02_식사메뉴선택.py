menu_list = [['자장면', 8000],
             ['제육볶음', 12000],
             ['스파게티', 11000],
             ['돈까스', 10000],
             ['라면', 5000],
             ['김밥', 3000]]

money = int(input("식대로 사용할 수 있는 금액: "))

print()
print("선택가능한 메뉴: ",end='')

for a in menu_list:
    if (a[1]<=money):
        print(a[0],end='  ')
