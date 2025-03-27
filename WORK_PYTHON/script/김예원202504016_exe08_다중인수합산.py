facts = []
total = 0
ordi = 1

while (True):
    d = input("%d번째 수 입력 : " %ordi)
    if d == '':
        break
    facts.append(int(d))
    total += int(d)
    ordi += 1

print()
for x in range(len(facts)-1):
    print(facts[x],end=' + ')
print(facts[-1],end=' = ')
print(total)
