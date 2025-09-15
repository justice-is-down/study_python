#사전은 키:값 형태로 되어있다.
#비슷한 자료구조로는 자바 스크립트 에는 오브젝트, 자바의 맵이 있다.
dic = {'name': 'Byeon sang-il', 'phone' : '010-7773-1312',
       'age':'39'}
print(dic['name'])
print(dic['phone'])
print(dic['age'])

dic2 = {
    'name':'Byeon sang-il',
    'phone':'010-7773-1312',
    'friends':['Alice','John','Smith']
}

#사전에 데이터 넣기1@ 둘다 알고있어야 한다
a = {'first':'a'}
print(a)
#사전에 데이터 넣기2 @ 둘다 알고있어야 한다
a['second'] = 'b'
print(a)

#사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전의 특정 요소를 꺼내보자 (사용법은 list와 비슷하다)
print(dic2['name'])
print(dic2['friends'])
#get 메서드를 활용해서도 가져올수 있다.
print(dic2.get('phone'))
#특정키가 없는 경우 None이 아닌 대체 내용으로 반환할수 있음
print(dic2.get('Nick','해당 내용이 없음'))
print(dic2.get('주소','그딴대모름'))

