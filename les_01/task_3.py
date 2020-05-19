# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти
# точки.

# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=QaxlUm1KiowSIK7YF7i3&title=les_01.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1ryvgAIWbVel7pYfdM-pzDalpAtoVc0lW%26export%3Ddownload

print('Введите координаты двух точек')
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

k = (y2 - y1) / (x2 - x1)
b = (y1*x2 - y2*x1) / (x2 - x1)

print(f'y = {k}*x + {b} (k = {k}, b = {b})')
