from file import read_dataset, write_dataset
from helper import print_result, print_commands, read_values
from manager import create, update, delete
from search import search_record

def main(file_path):
    print_commands()
    dataset = read_dataset(file_path)
    while True:
        command = input('Введіть команду зі списку: ')
        if command == 'new':
            values = read_values()
            dataset = create(dataset,values)
        elif command == 'sf':
            value = input('Введіть ім\'я: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sl':
            value = input('Введіть прізвище: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sfl':
            value = input('Введіть ім\'я: ')
            value_1 = input('Введіть прізвище: ')
            value = value + ' ' + value_1
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sp':
            value = input('Введіть номер телефону: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sct':
            value = input('Введіть місто: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sc':
            value = input('Введіть країну: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'up':
            values = read_values()
            dataset = update(dataset,values)
        elif command == 'del':
            dataset = delete(dataset)
        elif command == 'help':
            print_commands()
        elif command == 'exit':
            write_dataset(dataset, file_path)
            break
        else:
            print('Дана команда недоступна')



if __name__ == '__main__':
    main('database/database.json')
