from stack import Stack

check_balance = input('введите строку со скобками ')

brackets_list = Stack()

for i in check_balance:
    if brackets_list.size() != 0:
        if brackets_list.peek() == '[' and i == ']' or brackets_list.peek() == '(' and i == ')' or brackets_list.peek() == '{' and i == '}':
            brackets_list.pop()
            brackets_list.size()
        else:
            brackets_list.push(i)
    else:
        brackets_list.push(i)
if brackets_list.is_empty():
    print('«Сбалансированно»')
else:
    print('«Несбалансированно»')
