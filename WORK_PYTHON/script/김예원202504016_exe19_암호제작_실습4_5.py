st = input("암호화할 단어 입력 : ")
pw = ''

for x in st:
    temp_ch = ord(x)+3
    if temp_ch <= 122:
        pass_ch = chr(temp_ch)
        pw += pass_ch
    else:
        temp_ch -= 26
        pass_ch = chr(temp_ch)
        pw += pass_ch
print()

print(f"{st}의 암호문 : {pw}")
