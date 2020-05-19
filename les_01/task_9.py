# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=olDDV_0X1jn-2JmocPM4&title=les_01.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1ryvgAIWbVel7pYfdM-pzDalpAtoVc0lW%26export%3Ddownload

print('Введите три разных числа')
x = int(input())
y = int(input())
z = int(input())

if x > y:
    if x > z:
        if y > z:
            print(f'Среднее = {y}')
        else:
            print(f'Среднее = {z}')
    else:
        print(f'Среднее = {x}')
elif y > z:
    if x > z:
        print(f'Среднее = {x}')
    else:
        print(f'Среднее = {z}')
else:
    print(f'Среднее = {y}')
