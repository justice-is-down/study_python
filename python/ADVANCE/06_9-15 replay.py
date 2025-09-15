from asyncio import AbstractEventLoopPolicy

@매개변수 파라미터 *튜플 (수정불가)**딕셔너리(갯수가자유로움)
@인자값 아그먼트
def tuple_args
def dic_args
@매개변수 파라미터 = 함수 정의의 이름
함수 정의에서의 이름: 매개변수(파라미터)
예: def add(a, b): 여기서 a, b는 “이름표”입니다.

@인자값 아그먼트 = 호출시 넣는 실제값
함수 호출에서 넘기는 실제 값: 인자값(아규먼트)
예: add(2, 3)에서 2와 3이 “인자값”입니다.

인자값을 안주면
기본값이 있으면 그걸 쓰고, 없으면 오류가 납니다


@API =  Application Programming Interface의 약자.
무엇을, 어떻게 호출하면, 어떤 응답을 받는지”를 정해 놓은 사용 규칙과 그 집합입니다
개발자들 끼리의 손쉽게 만들어놓은 사용규칙과 집합을 설명한 사용설명서까지 포함

예시 ) 소프트웨어개발자 시선 아닌 일반인 컴퓨터유저입장시선
함수는 DOS라면
API는 윈도우 + 윈도우정품매뉴얼

@모듈 = 예시 )공구상자에서 필요한 도구를 모아두고 필요할떄 꺼내다 쓰는것
                  도구라 하면 함수, 변수, 클래쓰
from oper import sum
print(f'sum() 함수 실행 : {sum(5,10)}')
# import 모듈
# 일단 모듈을 불러놓고 모듈로부터 원하는 함수를 사용하는 방법
import oper as op
print(f'minus() 함수실행 : {op.minus(10,5)}')

@클래스
클래스는 설계도, 객체는 제품입니다.
속성은 데이터, 메서드는 행동입니다.
__init__은 만들 때 초기 설정, self는 현재 객체 자신
상속은 공통은 위로, 차이는 아래로 모아 재사용성이 높음

-클래스 안에 들어있는 속성과 메서드가 바로 멤버
-클래스는 멤버들을 정의하고, 객체는 그 멤버들의 실제 값을 가지며 동작

-일련번호가 서로 다르다.
-파이썬 에서도 객체화는 복사를 의미하므로 서로 다른 객체는 같지 않다.

-class Student: # Student 라는 클래스(학생과 관련된 함수 및 면수가 들어오겠구나 라고 예측 가능)
- pass # pass 는 함수나 클래스에 아무것도 없을때 오류방지를 위해 넣는 키워드






# 21. args ----------------------------
# 변수 입력 x시 입력해야 할 변수의 기본값 설정(error 방지)
def a (args=3):
-> a함수의 변수 기본값을 3으로 설정
-> 변수를 입력하지 않고 a()로만 실행하면 자동으로 변수에 기본값 3이 들어감
-> 변수를 입력하지 않았을 때의 오류 방지

# 인자값을 튜플로 받음 & 인자값의 개수 자유롭게
def b (*args):
-> b(1,3,4,5)로 넣으면 (1,3,4,5)처럼 tuple 형태로 들어감
-> 입력해야하는 인자값의 개수가 정해져 있지 않음 -> 원하는 만큼 넣을 수 있다. (변수 안 넣어도 오류 x)

# 인자값을 dictionary로 받음 & 인자값의 개수 자유롭게
def c (**args):
-> c(key=value, key=value, key=value.....)
-> c(kim=80, lee=90)으로 넣으면 kim,lee가 key, 80,90이 각각의 key에 해당하는 value로 dictionary 형태로 입력됨
-> {kim:80, lee:90}처럼 dictionary 형태로 들어감
-> 입력해야 하는 인자값의 개수가 정해져 있지 않음 -> 원하는 만큼 넣을 수 있다. (변수 안 넣어도 오류 x)

# 22. API ----------------------------
# API(Aplication Programming Interface)
"""
:param x : ~~~
"""
-> def로 정의되는 함수 안에 """ """를 입력하면 자동으로 파라미터 설명 입력할 수 있게 뜸
-> parameter, return값, function 기능 설명 등 누구나 사용할 수 있게 적는 설명서

print({a.__doc__})
-> .__doc__를 사용하여 설명서 확인 가능

# 01. module 불러오기 ----------------------------
# module : 여러 파일에서 가져다 쓸 수 있는 공통의 기능
from module import function
-> 특정 module에서 특정 함수 하나만 불러오는 방법
-> module에서 불러와야 하는 함수가 몇 개 없을 때 유용!
-> 불러온 함수 사용 : function()로 바로 사용 가능

import module (as module_약어)
-> 특정 module 전체를 불러오는 방법
-> module에서 불러와야 하는 함수가 많을 때, 함수를 일일이 불러오지 않고 한 번에 사용할 수 있다.
-> 불러온 함수 사용 : module.function()으로 사용해야 함!

# 02. module 확인하기 ----------------------------
# 특정 module에 정의되어 있는 변수, 함수들의 목록 확인하기
print(dir(oper))
내장함수 dir() : dir()의 변수로 특정 module 이름을 넣으면 해당 module 안에 있는 변수와 함수들의 목록을 list로 반환

# 특정 module의 이름 확인
.__name__ : . 앞에 있는 특정 module의 이름 확인
ex)
import pandas as pd
print(pd.__name__) # pandas

__name__ : 현재 나의 이름 -> 현재 실행되는 함수의 이름 확인

# 03. class ----------------------------
class Home:
-> class 이름은 항상 첫글자 대문자 & class 안의 변수, 함수를 대표할 수 있는 단어로 class name 설정

home1 = Home()
home2 = Home()
-> class Home을 객체화(복사)하여 객체 home1, home2으로 반환
-> Home은 class 원본(STATIC 영역), home은 instance 복사본(HEAP 영역)

print(home1)
print(home2)
-> 둘 다 class Home을 객체화한 것이지만, 서로 다른 복사본
-> 각각 print() 해보면 일련번호가 다름!

# 04. class의 member ----------------------------
# class의 member : class 안에 있는 것, constructor, variable, function이 있음

# field : class member인 변수variable

# constructor : 생성자
def __init__(self):
-> class인 Home을 객체화하는 Home()을 실행하면 constructor가 객체화, 초기화(초기값 설정)하는 역할
-> class를 객체화할 때 처음 한 번만 실행됨
def __init__ (self, name, location)
-> self 이외에도 class에서 설정한 변수를 입력값으로 같이 받을 수 있다. name, location 등
-> 단, 그냥 입력 받을 경우 ex) home = Home('집', '서울')
-> 객체화하면 생성자를 실행하고 난 뒤에 끝남 (생성자는 class 안에 있으므로 생성자에서 입력받은 변수는 class 밖으로 나갈 수 없음)
-> 입력받은 값을 생성자 밖에서(class 전체에서) 사용할 수 있도록 class member인 변수에 넣어주는 과정이 필요
-> self가 해당 class를 의미하므로 self.name이라고 쓰면 class의 name, 즉 class member변수인 name으로 인식
-> self.name = name -> 입력받은 name을 class 변수인 self.name에 저장
-> 입력받은 값을 생성자 안에서만이 아니라 class 전체에서 사용할 수 있음

# function : class member인 함수
def function_name(self,a,b...):
-> class 내 함수도 생성자와 마찬가지로 항상 self를 인자로 갖는다.
