##6) *Реализовать структуру данных «Товары».

goods = []
features = {'имя': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'имя': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input(
        "Для выхода введите 'q', Чтобы ввести товар нажмите 'Enter', "
        "для вывода аналитики введите 'a'")
    if control == 'q':
        break
    num += 1
    if control == 'a':
        print('Аналитика')
        for key, value in analytics.items():
            print(f'{key}: {value}')

    for f in features.keys():
        feature_ = input(f'Введите параметр {f} ')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))