st = input("문장 입력 : ")
word = st.split(' ')

print("총 글자 수 : %d자" %len(st))
print("공백 수 : %d개" %st.count('  '))
print()
print(word)
print("단어 수 : %d개" %len(word))
