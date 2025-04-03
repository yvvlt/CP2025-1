mbti_type = {"INTJ": "용의주도한 전략가형", 
"INTP": "논리적인 사색가형",
"ENTJ": "대담한 통솔자형",
"ENTP": "뜨거운 논쟁을 즐기는 변론가형",
"ENFP": "재기발랄한 활동가형",
"ENFJ": "정의로운 사회 운동가형",
"INFP": "열정적인 중재자형",
"INFJ": "선의의 옹호자형",
"ESFJ": "사교적인 외교관형",
"ESTJ": "엄격한 관리자형",
"ISFJ": "용감한 수호자형",
"ISTJ": "청렴결백한 논리주의자형",
"ESFP": "자유로운 영혼의 연예인형",
"ESTP": "모험을 즐기는 사업가형",
"ISFP": "호기심 많은 예술가형",
"ISTP": "만능 재주꾼형"
}

mbti_job = {
"INTJ": "투자 은행원, 재무상담가, SW개발자",
"INTP": "프로그래머, 재무 분석가, 교수",
"ENTJ": "변호사, 경영 컨설턴트, 분석 전문가",
"ENTP": "기업가, 정치가, 마케팅 디렉터",
"ENFP": "저널리스트, 요식업 경영자, 파티플래너",
"ENFJ": "세일즈 매니저, 고용 전문가, PR 전문가",
"INFP": "그래픽 디자이너, 심리학자, 작가",
"INFJ": "치료사, 사회복지사, 고객 관계 매니저",
"ESFJ": "판매 대표자, 간호사, 헬스케어 종사자",
"ESTJ": "보험 세일즈맨, 약사, 프로젝츠 매니저",
"ISFJ": "치과의사, 사서, 초등학교 교사",
"ISTJ": "감리사, 회계사, 웹 개발자",
"ESFP": "아동 복지 상담가, 배우 , 디자이너",
"ESTP": "탐정, 은행원, 투자가",
"ISFP": "패션 디자이너, 물리치료사, 조경설계사",
"ISTP": "토목기사, 파일럿, 경제학자"}

mbti_good = {
"INTJ": "ESFP",
"INTP": "ESFJ",
"ENTJ": "ISFP",
"ENTP": "ISFJ",
"ENFP": "ISTJ",
"ENFJ": "ISTP",
"INFP": "ESTJ",
"INFJ": "ESTP",
"ESFJ": "INTP",
"ESTJ": "INFP",
"ISFJ": "ENTP",
"ISTJ": "ENFP",
"ESFP": "INTJ",
"ESTP": "INFJ",
"ISFP": "ENTJ",
"ISTP": "ENFJ"
}

mbti_bad = {
"INTJ": "ESFJ",
"INTP": "ESFP",
"ENTJ": "ISFJ",
"ENTP": "ISFP",
"ENFP": "ISTP",
"ENFJ": "ISTJ",
"INFP": "ESTP",
"INFJ": "ESTJ",
"ESFJ": "INTJ",
"ESTJ": "INFJ",
"ISFJ": "ENTJ",
"ISTJ": "ENFJ",
"ESFP": "INTP",
"ESTP": "INFP",
"ISFP": "ENTP",
"ISTP": "ENFP"    
}

print('MBTI TEST')
print()
answer=''
print("※ 각 문항에 대해 예, 아니오로 답해주세요")
Q1=int(input('1. 다른 사람들에게 자신을 소개하는 것을 어려워 합니다.(예=0, 아니오=1) : '))
Q2=int(input('2. 논쟁에서 이기는 것이 상대방을 불쾌하지 않도록 하는 것보다 더 중요합니다.(예=0, 아니오=1) : '))
Q3=int(input('3. 적응을 잘 하는 것 보다 체계적인 것이 더 중요합니다.(예=0, 아니오=1) : '))
Q4=int(input('4. 본인이 창의적이기보다 현실적인 사람이라고 생각합니다.(예=0, 아니오=1) : '))
print('\n\n')

answer += 'I' if Q1==0 else 'E'
answer += 'S' if Q4==0 else 'N'
answer += 'T' if Q2==0 else 'F'
answer += 'J' if Q3==0 else 'P'

for x in mbti_type.keys():
    if answer==x:
        print(f"타입 : [ {x} ] {mbti_type[x]}")
print()
for x in mbti_job.keys():
    if answer==x:
        print(f"직업 : [ {x} ] {mbti_job[x]}")
print()
for x in mbti_good.keys():
    if answer==x:
        print(f"잘 맞는 유형 : [ {mbti_good[x]} ] {mbti_type[mbti_good[x]]}")
print()
for x in mbti_bad.keys():
    if answer==x:
        print(f"맞지 않는 유형 : [ {mbti_bad[x]} ] {mbti_type[mbti_bad[x]]}")














