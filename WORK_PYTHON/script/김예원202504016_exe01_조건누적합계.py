start = int(input("누적합계 시작값 입력: "))
end = int(input("누적합계 끝값 입력: "))
total = 0

for step in range(start, end+1):
    if (step%2 == 0):
        total +=step

print()
print("%d부터 %d까지의 짝수누적합계 : %d"%(start,end,total))

    
