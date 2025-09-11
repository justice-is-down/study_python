#검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는것
import builtins
from os import remove

a= [3,4,1,2,3,4,'G','F','G']
#원하는 값의 인덱스 찾기
# 2라는 값은 어느 위치에 있는가?
print(f'2는 어디?:{a.index(2)}')
print(f'2는 어디?:[{a.index('G')}]') #G는 2개이지만 처음 찾은 값만 알려준다

# 5번인덱스부터'G'를 찾아라
print(f'G는 어디?:{a.index('G',5)}')
#값이 없으면 에러 (예외)를 발생 시킨다.
#print{a.index('H')} #ValueError: 'H' is not in list

print(f'2는 어디?:[{a.index('G')}]')



b = [3,4,1,2,3,4,1,2,3]
#@@승연님의 특별강의@@
idx = 0
while True:
    idx = b.index(3,idx)
    print(f'3의값은 {idx}번에 있다.')
    idx +=1

#@@승연님의 특별강의@@
b = [3, 4, 1, 2, 3, 4, 5, 6, 1, 3, 2]  # 모든 3을 찾아 보세요.

# idx = b.index(3,0)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,1)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,5)
# print(f'3의 값은 {idx}번에 있다.')

idx = 0  # idx 초기값을 0으로 설정
while True:  # True면 계속 실행
    idx = b.index(3, idx)
    # index()함수로 b에서 값이 3인 index를 b[idx]부터 찾음 -> 찾은 index를 idx값으로 저장
    # ex) idx = 0부터 -> b.index(3,0) -> 찾은 index값은 0을 idx에 대입 -> idx = 0

    print(f'3의 값은 {idx}번에 있다.')  # 찾은 index값을 출력
    idx += 1  # 찾은 index값이 초기값과 같다면 다시 초기값부터 값이 3인 index를 찾으므로

    # 찾은 index 다음 index부터 검색할 수 있도록 idx에 1을 더해줌

    # 값이 3인 index를 찾고, 해당 index를 idx에 저장&출력 -> idx + 1인 index부터 다시 3을 찾음 -> 반복

    # idx 초기값 = 0 -> idx = b.index(3,0) -> b[0]부터 값이 3인 index를 찾아서 idx값으로 저장 -> idx = 0 -> idx +=1 -> idx = 1
    # idx = 1 -> idx = b.index(3,1) -> b[1]부터 값이 3인 index를 찾아서 idx값으로 저장 -> idx = 4 -> idx +=1 -> idx = 5
    # idx = 5 -> idx = b.index(3,5) -> b[5]부터 값이 3인 index를 찾아서 idx값으로 저장 -> idx = 9 -> idx +=1 -> idx = 10
    # idx = 10 -> 그 뒤부터는 3이 없음 -> ValueError : 3 is not in list

    # for문보다 효율적, for문은 처음부터 마지막 index까지 하나하나 확인하지만 (len(b)번 만큼 반복해야 함)
    # 이렇게 하면 값이 3인 index를 찾고, 다음에 찾을 때는 그 뒤부터 찾으면 된다!! (3개수 + 1번 만큼만 반복해도 됨)

    if b[len(b) - 1] != 3:
        break

##@@다날라감 다시 공부하세요 변상일

#리스트 요소 삭제
#del a[3] 과 a.remove(3)
#del 은 특정 인덱스의 값을 지운다
#remove는 해당 값을 지운다.(한개만)

# print(f'a:{a}')
# a.remove(3)
# print(f'a:{a}')

#pop() = append() 의 반대개념
#맨 마지막 요소를 빼낸다.(리스트에서는 사라진다는 의미)
# val = a.pop()
# print(f'빼낸값:{val}/a:{a}')
# val = a.pop()
# print(f'뺴낸값:{val}/a:{a}')

#리스트 확장 (더하기와 비슷한 개념)
# print(a)
# a.extend(b)
# print(a)

#cont(val) 특정한 값이 해당 리스트에 몇개 있는지 확인
# print(a)
# print(f'a안에 3인{a.count(3)}개 가 있다.')
# print(f'a안에 9인{a.count(9)}개 가 있다.') #없는값은 0을 반환

#a안에 있는 모든 3을 지워주세요
# for n in a:
#     if n == 3:
#         a.remove(3)

# while True:
#     a.remove(3)
#     if a.count(3)==0:
#         break


