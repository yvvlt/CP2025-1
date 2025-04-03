a = {x for x in range(2,101,2)}
b = {y for y in range(3,101,3)}

print('1~100까지 2와 3의 배수의 개수 : ',len(a.union(b)))
print(a.union(b))
print()
print('1~100까지 2와 3의 공배수의 개수 : ',len(a.intersection(b)))
print(a.intersection(b))
