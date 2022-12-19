import view


def parser_number():
    number = view.input_number()
    list1 = number.split()
    ptjer = len(list1)
    print(list1)
    print(ptjer)
    if len(list1) > 1:
        print(len(list1))
        print(list1)
        return True



def parse_str():
    string = view.input_number()
    # string = '4 + 4 * 4'
    print(string)
    list = string.split()
    print(list)
    for i in range(len(list)):
        if list[i].isdigit():
            list[i] = int(list[i])
    print(list)

    result = 0

    while len(list) !=1:
        i = 0
        while ('*' in list or '/' in list) and i < len(list):
            if list[i] == "*":
                result = list[i-1] * list[i+1]
                list.pop(i)
                list.pop(i)
                list[i-1] = result
                i -= 1
            elif list[i] == "/":
                result = list[i-1] / list[i+1]
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i -= 1
            i +=1
            print(list)
        while ('+' in list or "-" in list) and i < len(list):
            if list[i] == '+':
                result = list[i - 1] + list[i + 1]
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i -= 1
            elif list[i] == '-':
                result = list[i - 1] - list[i + 1]
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i -= 1
            i += 1
            print(list)
