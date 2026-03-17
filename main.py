# 파일이름 :
# 작 성 자 :
# 미션 1
name3 = input('이름을 입력하시오: ')
writing3 = int(input('당신의 글쓰기 점수를 입력하시오: '))
python3 = int(input('당신의 파이썬 점수를 입력하시오: '))
last_avg3 = float(input('지난학기 평균: '))

average3 = (writing3 + python3) / 2

print(f'\n{name3} 학생의 글쓰기 점수는 {writing3}, 파이썬 점수는 {python3} 입니다.')
print(f'평균은 {average3} 이고, 지난 학기와 차이는 {average3 - last_avg3}입니다.')
