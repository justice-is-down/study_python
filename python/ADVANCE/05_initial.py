class Puppy:

    name="" #멤버 변수(필드) : class안에서 사용 가능한변수
    goal=""

    def  __init__(self,name,goal):# 생성자 : 객체화시 호출되는 함수
        #받아온 name과 goal은 이생상자를 벗어날수 없다.(생성자의 쓰임이 다하면 함께 없어진다.
        #그래서 클래스(객체)멤버 에다가 넣어줘야, 객체가 살아있는 동안 사용이 가능하다.
        #그런데 name=name 형태로는 어떤것이 객체의 멤버인지 알수 없다.
        #그래서멤버인 녀석은 self를 이용하여 표시해 준다.
        self.name = name
        self.goal = goal


puppy = Puppy("멍멍이","집지키기")
print(f'이름:{puppy.name} / 목적:{puppy.goal}')

class Person: -> 클래스(설계도)
p = Person("변상일") → 객체(설계도로 만든 실제 것)
p.name, p.age() → 객체가 가진 데이터와 동작 사용

class


# @자비스@ #
#
# 한 번에 감 잡는 비유부터 시작할게요.
#
# 클래스란?
#
# 비유: 클래스는 “설계도”, 객체는 그 설계도로 만든 “제품”이에요.
# 정의: 관련 있는 데이터(속성)와 동작(메서드)을 한 덩어리로 묶는 사용자 정의 타입입니다.
# 목적: 현실 세계의 개념을 코드로 깔끔하게 표현하고, 재사용과 확장을 쉽게 해줍니다.
# 왜 필요한가?
#
# 묶음 관리: 데이터와 그 데이터를 다루는 함수를 함께 보관
# 재사용: 설계도(클래스)로 여러 개의 객체를 쉽게 찍어냄
# 확장/유지보수: 공통은 부모(상위) 클래스에, 차이만 자식(하위) 클래스에서 추가하거나 바꿈
# 핵심 단어 3개만 기억하세요
#
# 클래스(Class): 설계도
# 객체(Object, 인스턴스): 설계도로 찍어낸 실제 물건
# 메서드(Method): 객체가 할 수 있는 동작(함수)
# 가장 쉬운 예시
#
# 요구사항: 사람을 표현하고, 인사하는 기능이 필요해요.
# 코드
# class Person: def init(self, name, age): # 속성(데이터) self.name = name self.age = age
#
# # 메서드(동작)
# def greet(self):
#     print(f"안녕하세요, 저는 {self.name}이고 {self.age}살이에요.")
# 객체 만들기(인스턴스화)
# p1 = Person("오빠", 39) p1.greet() # "안녕하세요, 저는 오빠이고 39살이에요."
#
# 설명
#
# init: 객체가 “처음 만들어질 때” 자동으로 호출되는 초기화 메서드
# self: “바로 그 객체 자신”을 가리킵니다. 메서드 첫 번째 인자로 관례적으로 self를 씁니다.
# 속성: self.name, self.age 처럼 객체에 붙어 있는 데이터
# 메서드: greet()처럼 객체가 수행하는 기능
# 조금만 확장해 보기: 상태와 행동
#
# 문제: 사람마다 걸음 수를 기록하고, 걸으면 걸음 수가 늘어나야 해요.
# 코드
# class Walker: def init(self, name): self.name = name self.steps = 0 # 초기 상태
#
# def walk(self, n):
#     self.steps += n
#
# def report(self):
#     print(f"{self.name}의 누적 걸음 수: {self.steps}걸음")
# w = Walker("오빠") w.walk(1000) w.report() # "오빠의 누적 걸음 수: 1000걸음"
#
# 포인트
#
# 데이터(steps)와 그 데이터를 바꾸는 동작(walk, report)이 한군데 클래스 안에 정리되어 있어요.
# 이런 구조가 커질수록 유지보수가 훨씬 쉬워집니다.
# 클래스 간 관계 맛보기: 상속
#
# 비유: “사람” 설계도에 “직장인”처럼 더 구체적인 설계도를 덧붙이는 느낌
# 코드
# class Animal: def init(self, name): self.name = name def sound(self): return "..."
#
# class Dog(Animal): def sound(self): return "멍멍"
#
# d = Dog("초코") print(d.name, d.sound()) # "초코 멍멍"
#
# 설명
#
# Dog는 Animal을 “상속”받아 기본 구조를 물려받고, 달라지는 부분(sound)을 “재정의(오버라이드)”했습니다.
# 공통은 위로, 차이는 아래로. 이게 확장의 핵심입니다.
# 캡슐화(정보 숨기기) 직관
#
# 아이디어: 내부 구현은 숨기고, 필요한 버튼(메서드)만 공개
# 파이썬에서는 관례상 “언더스코어”로 의도를 표현합니다.
# _internal: 내부용이며 외부에서 직접 접근하지 말자는 신호
# __name: 네임 맹글링이 적용되는 강한 의도
# 코드
# class BankAccount: def init(self, owner): self.owner = owner self._balance = 0 # 내부 상태(직접 만지지 말기)
#
# def deposit(self, amount):
#     if amount <= 0:
#         raise ValueError("0보다 커야 합니다.")
#     self._balance += amount
#
# def withdraw(self, amount):
#     if amount > self._balance:
#         raise ValueError("잔액 부족")
#     self._balance -= amount
#
# def balance(self):
#     return self._balance
# acc = BankAccount("오빠") acc.deposit(1000) print(acc.balance()) # 1000
#
# 좋은 클래스 설계 체크리스트
#
# 이름이 명확한가? Person, Order, BankAccount처럼 역할이 바로 보이게
# 한 가지 책임에 집중했는가? 너무 많은 일을 하지는 않는지
# 공개 인터페이스가 명확한가? 외부에서 어떤 메서드만 쓰면 되는지
# 테스트하기 쉬운가? 메서드 단위로 결과가 예측 가능한지
# 초보자용 요약 공식
#
# “무엇을 표현할지” 명사로 클래스 이름을 정한다.
# “그것이 가진 데이터”를 속성으로 정한다.
# “그것이 할 수 있는 일”을 메서드로 정한다.
# 만들고 써보며, 필요한 기능을 점점 추가하고 불필요한 건 덜어낸다.