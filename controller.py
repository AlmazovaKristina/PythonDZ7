import view
import model
import parser


def input_first():
    number = view.input_number()
    model.set_first(number)


def input_second():
    while True:
        number = view.input_number()
        if model.ger_operation() == '/' and number == 0:
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break


def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
    oper = model.ger_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper =='/':
        model.division()

    result_string = f'{model.ger_first()} {model.ger_operation()} {model.ger_second()} = {model.ger_result()}'
    view.print_to_console(result_string)
    model.set_first(model.ger_result())


def start():
    g = parser.parser_number()
    print(g)
    if g != True:
        input_first()
        while True:
            input_operation()
            if model.ger_operation() == '=':
                view.log_off()
                break
            input_second()
            solution()
    else:
        parser.parse_str()
