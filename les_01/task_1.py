# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=les_01.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1ryvgAIWbVel7pYfdM-pzDalpAtoVc0lW%26export%3Ddownload

print('Введите трехзначное число')
a = int(input())

d1 = a // 100
a = a % 100
d2 = a // 10
d3 = a % 10

s = d1 + d2 + d3
m = d1 * d2 * d3

print(f'сумма = {s}')
print(f'произведение = {m}')
