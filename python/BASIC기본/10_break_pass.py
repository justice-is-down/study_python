cup = 0
running = True

# while True:
#     cup += 1
#     print(cup)
#     if cup == 10:
#         #running = False
#         break

print('while 문 종료')

for i in range(1,10):
    if i == 3:
        continue
    if i == 6:
        continue
    if i == 9:
        continue
    print(i)