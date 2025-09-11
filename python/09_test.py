import random #@무작위밖에모르겟음

number = random.randint(1,31)
print(f' 내 마음속 숫자:{number}') #@내마음속의 숫자 {랜덤몇번}
running = True #@조건을 충족할떄까지 러닝시작

while running: #@정해져 있지않음의 무한반복
    #입력받은 값을 정수(int) 로 변환하여 guess에 대입
    guess = int(input('1~31 중 내가 생각한 숫자는?')) #@내마음속의 숫자 {랜덤몇번}
    print(f'입력받은 숫자:{guess}')
    if guess == number: #@이프 입력받은숫자와 내가 생각하는 숫자가 같다
        running = False #@ 조건이 충족할시 러닝끝
        print(f'내마음속 숫자{number}와 입력받은숫자{guess}가 같습니다.')#@조건충족 요건
    elif guess < number:
        print(f'내마음속 숫자{number}와 입력받은숫자{guess}가 적습니다.')#@ 조건 다른요인
    elif guess > number :
        print (f'내마음속 숫자{number}와 입력받은숫자{guess}가 많습니다.')#@ 조건 다른요인


