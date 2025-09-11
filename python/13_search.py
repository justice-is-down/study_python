#검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는것
import builtins

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

idx = 0
while True:
    idx = b.index(3,idx)
    print(f'3의값은 {idx}번에 있다.')

##@@다날라감 다시 공부하세요 변상일