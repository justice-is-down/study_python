#인자값으로 아무것도 들어오지 않ㅇ았을 경우 에러를 방지하기 위해 기본값 설정이 가능
def plus(num=0):
    resutl = num + 5
    return resutl

print(plus(5)) # 10
print(plus()) #plus() missing 1 required positional argument: 'num'