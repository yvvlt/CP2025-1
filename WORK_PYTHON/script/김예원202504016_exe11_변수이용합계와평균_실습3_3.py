name1 = input('첫 번째 학생 성명 입력 : ')
score1 = int(input(f'{name1}의 점수 입력 : '))
print()

name2 = input('두 번째 학생 성명 입력 : ')
score2 = int(input(f'{name2}의 점수 입력 : '))
print()

name3 = input('세 번째 학생 성명 입력 : ')
score3 = int(input(f'{name3}의 점수 입력 : '))
print()


total = score1 + score2 + score3
average = total/3

print(f'첫 번째 학생의 성명 : {name1}, 첫 번째 학생의 점수 : {score1}')
print(f'두 번째 학생의 성명 : {name2}, 두 번째 학생의 점수 : {score2}')
print(f'세 번째 학생의 성명 : {name3}, 세 번째 학생의 점수 : {score3}')
print(f'합계 : {total}점, 평균 : {average:.2f}점')
