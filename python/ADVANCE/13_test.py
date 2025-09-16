# import traceback
#
# text =('값을 넣으면 숫자로 변환 됩니다.')
# num = int(text)
# print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
#
# try:
#     text =input('값을 넣으면 숫자로 변환 됩니다.')
#     num = int(text)
#     print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
#
# except Exception as e:
#     print('숫자를쓸수없습니다.')
#     print('f에러 : {e}')
#     traceback.print_exc()
# finally:
#      print('====끝====')

while True:
    try:
        text = input('값을 넣으면 숫자로 변환 됩니다.')
        num = int(text)
        print(f'당신이 입력한 값:{num}이 숫자로 변환 되었습니다.')
        break
    except ValueError :
        print(f'{text}는 숫자가 아닙니다.');