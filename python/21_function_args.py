#인자값으로 아무것도 들어오지 않ㅇ았을 경우 에러를 방지하기 위해 기본값 설정이 가능
from ctypes import HRESULT


def plus(num=0):
    resutl = num + 5
    return resutl

print(plus(5)) # 10
print(plus()) #plus() missing 1 required positional argument: 'num'

#인자값의 종류를 튜플(수정이 불가능한  List 형태) 로만 받겟다.
def tuple_args(*numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    return total
# 이 방식은 사용자가 인자값의 갯수를 자유롭게 정해서 넣을 수 있다.
print(tuple_args(1,2,3,4,5))

# ** 는 매개변수를 사전형태로 받겠다.
def dic_args(**dic):
    #1. dic 에서 값만 빼온다.
    values = dic.values()
    print(values)
    #2. 이값들을 하나씩 더해 누적시킨다.
    total = 0
    for v in values:
        # print(v)
        total += v
    #3. 누적시킨값을 밖으로 return한다.
    return total

     print(dic)

    result = 0
    for key in dic.keys():
        result += dic. get(key)
    print(result)

    result2 = 0
    for value in dic.values():
        result2 += value
        print(result2)

    result3 = 0
    for item in dic.items():
        result3 += item[1]
        print(result3)




# 위 함수를 실행하면 입력된 값들의 합산이 반한되도록 하세요
result = dic_args(kim=50, lee=100, park=70, na= 90)
print(result)
