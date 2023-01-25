input = '12 / 4 - 3 * 14 + 45 * 3 - 78 + 30 / 6'

input_list = input.split()

def calc (num1, action, num2):
    if action == '+': return num1 + num2
    if action == '-': return num1 - num2
    if action == '*': return num1 * num2
    if action == '/': return num1 / num2



def action(input_list):
    for i in range(len(input_list)):
        if input_list[i] == '*' or input_list[i] == '/':
            num1 = int(input_list[i-1])
            action = input_list[i]
            num2 = int(input_list[i+1])
            print(num1, action, num2,'=', calc(num1, action, num2))
            input_list[i] = calc(num1, action, num2)
            input_list.pop(i-1)
            input_list.pop(i)
            input_list.insert(0, None)
            input_list.insert(0, None)
    for i in range(len(input_list)):
        if input_list[i] == '+' or input_list[i] == '-':
            num1 = int(input_list[i-1])
            action = input_list[i]
            num2 = int(input_list[i+1])
            print(num1, action, num2,'=', calc(num1, action, num2))
            input_list[i] = calc(num1, action, num2)
            input_list.pop(i-1)
            input_list.pop(i)
            input_list.insert(0, None)
            input_list.insert(0, None)
    print(input, '=', input_list.pop())
    return(action(input_list))
action(input_list)
