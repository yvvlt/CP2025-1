x = 0
sdb = []

while (True) :
    sdb += [[]]
    sdb[x].append(input("%d번째 학생 성명 입력 : " %(x+1)))
    if sdb[x][0] == '':
        sdb.pop(x)
        break
    sdb[x].append(int(input("%s의 국어점수 입력 : " %sdb[x][0])))
    sdb[x].append(int(input("%s의 영어점수 입력 : " %sdb[x][0])))
    sdb[x].append(int(input("%s의 수학점수 입력 : " %sdb[x][0])))
    sdb[x].append(int(input("%s의 물리점수 입력 : " %sdb[x][0])))
    sdb[x].append(sdb[x][1]+sdb[x][2]+sdb[x][3]+sdb[x][4])
    x += 1

print()
print(" 성명\t국어\t영어\t수학\t물리\t합계")
print("-----\t"*6)

for x in range(len(sdb)):
    for y in range(len(sdb[0])):
        print(sdb[x][y],end='\t')
    print()




