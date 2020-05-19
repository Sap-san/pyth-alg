# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=u2srGoAEU2hbk21t9wgX&title=les_01.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1ryvgAIWbVel7pYfdM-pzDalpAtoVc0lW%26export%3Ddownload

print('Введите год')
y = int(input())

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print('Год високосный')
        else:
            print('Год невисокосный')
    else:
        print('Год високосный')
else:
    print('Год невисокосный')