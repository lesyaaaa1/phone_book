from helper import read_values

def create(dataset: dict, data: dict):
    dataset.update(data)
    return dataset

def update(dataset: dict, data: dict):
    # input phone number - result = read_values() - значення, які не порожні -> замінюємо
    # find record by number
    # update record
    for key_1,value_1,key_2,value_2 in zip(data.keys(),data.values(),dataset.keys(),dataset.values()) :
        for key_3,value_3,key_4,value_4 in zip(value_1.keys(),value_1.values(),value_2.keys(),value_2.values()):
            if value_3 == '':
                data[key_1][key_3]=value_4
        dataset.update(data)
    else:
        dataset.update(data)
    return dataset


def delete(dataset: dict):
    # input phone number
    # delete if exist
    phone = input('Введіть номер телефону: ')
    if phone in dataset:
        del dataset[phone]
        print('Номер видалено')
    else:
        print('Такого номеру не існує')
    return dataset
