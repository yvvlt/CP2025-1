jumsoo = []
c = 1
total = 0

while True:
    j = input(f'{c}번째 학생의 점수 입력 : ')
    if j == '':
        break
    jumsoo.append(int(j))
    c += 1

for x in jumsoo:
    total += x

average = total/len(jumsoo)

print()
print('입력된 점수 : ',end='')
for y in jumsoo:
    print(y,end='  ')
print()
print(f'합계 : {total}점, 평균 : {average:.2f}점')
