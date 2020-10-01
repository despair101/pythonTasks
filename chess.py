import math

def GetWeight(cornAmount):
    return cornAmount / 2e8

def LayersAmount(cornAmount, cornArea, area):
    return int(cornAmount * cornArea // area)

def GetTime(cornAmount, cornAmountPerYear):
    return math.ceil(cornAmount / cornAmountPerYear)
    
counter = 0
cornAmount = 0
price = 1
while counter < 64:
    counter += 1
    cornAmount += price
    price *= 2
print('Правитель должен был заплатить изобретателю', cornAmount, 'зёрен')
go = True
while go:
    command = input('Введите, что вы хотите узнать: массу зёрен; количество слоёв зёрен на территории; время, за которое они будут выращены.\n')
    if command == 'массу зёрен':
        print(GetWeight(cornAmount), 'тонн')
    elif command == 'количество слоёв зёрен на территории':
        cornArea = float(input('Введите площадь поверхности зёрнышка в м^2: ')) / 2
        area = int(input('Введите площадь территории в м^2: '))
        print(LayersAmount(cornAmount, cornArea, area), 'слоёв')
    elif command == 'время, за которое они будут выращены':
        cornAmountPerYear = int(input('Введите количество зёрен, выращиваемое за год: '))
        print('Потребовалось бы', GetTime(cornAmount, cornAmountPerYear), 'лет')
    else:
        go = False
