base_dict = {
    'phone_number': {
        'first_name': '',
        'last_name': '',
        'city': '',
        'country': '',
    }
} # dataset example structure

keys = ['first_name', 'last_name', 'city', 'country']
values = ['ім\'я','прізвище','місто','країна']

def print_commands():
    print('Доступні команди:',
          'new - створити новий запис',
          'sf - пошук за ім\'ям',
          'sl - пошук за прізвищем',
          'sfl - пошук за повним іменем',
          'sp - пошук за телефоном',
          'sct - пошук за містом',
          'sc - пошук за країною',
          'up - оновлення',
          'del - видалення',
          'help - список доступних команд',
          'exit - вихід з програми',sep='\n')



def print_result(result):
    for phone, data in result.items():
        print(f'Номер телефону: {phone} ')
        for name, record in zip(values, data):
            print(f'\t{name.capitalize()}: {data[record]}')

def read_values():
    phone = input('Введіть номер телефону: ')
    new_data = {phone: {}}
    for key,value in zip(keys, values):
        new_data[phone][key] = input(f'Введіть {value}: ')
    return new_data








