def input_number():
    while True:
        # try:
            number = input('Введите  целое число: ')
            return number
        # except:
        #     print('Ошибка')





def input_operation():
    while True:
        operation = input('Введите  операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию')

def print_to_console(value_text):
    print(value_text)

def log_off():
    print('До свидания!')

def print_division_by_zero():
    print('На ноль делить нельзя')

# def parser():
#     print(parser())