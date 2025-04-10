print('*')
print('**')
print('***')
print('****')
print('*****')
print()

print('*'*1)
print('*'*2)
print('*'*3)
print('*'*4)
print('*'*5)
print()

for x in range(1,11):
    print('*'*x)
print()

print(' '*4 + '*'*1)
print(' '*3 + '*'*2)
print(' '*2 + '*'*3)
print(' '*1 + '*'*4)
print(' '*0 + '*'*5)
print()

for x in range(1,11):
    print(' '*(10-x)+'*'*x)
