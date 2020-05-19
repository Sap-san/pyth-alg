# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.

# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=NOhqcklfU36Y5H2EDRj2&title=les_01.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1ryvgAIWbVel7pYfdM-pzDalpAtoVc0lW%26export%3Ddownload

print('Введите длины трех отрезков')
a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    if a == b:
        if a == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    elif a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Нельзя построить треугольник')
