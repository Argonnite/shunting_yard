'''
Example 1a:  (2 - 3 * 4) / (9 / 5 + 6 * (-14 / 2)) - 3
Example 1b:  -(4 - 3)/ 4 * (3 - 4 * -2)
Example 2:  (2 | 3 * 4) / (9 & 5 + 6 | (-14 / 2)) & 3

& = min operator, | = max operator
Operator precedence:
| and &
* and /
+ and -

'''


#s = "(6- 3 * 4) / (9 / 5 + 6 * (-14 / 2)) - 3"
s = "(6 * 3 - 4) / (9 / 5 + 6 * (-14 / 2)) - 3"
#s = "6 * 3 - 4 / (9 / 5 + 6 * (-14 / 2)) - 3"
#s = "6 - 3 * 4 / (9 / 5 + 6 * (-14 / 2)) - 3"


'''PSEUDOCODE, PART 1
while token = get_token(s):
    if is_number(token):
        output_queue.append(token)
    if is_operator(token):
        while (has_precedence(operator_stack[-1], token)
               or has_equal_precedence_but_left_associative(operator_stack[-1]))
               and operator_stack[-1] != '(':
            output_queue.append(operator_stack.pop())
        operator_stack.append(token)
    if token == '(':
        operator_stack.append(token)
    if token == ')':
        while operator_stack[-1] != '(':
            output_queue.append(operator_stack.pop())
        if operator_stack[-1] == '(':
            operator_stack.pop()
while len(operator_stack) > 0:
    output_queue.append(operator_stack.pop())
'''
from fractions import Fraction

def has_precedence(token1, token2):
    return (token1 == "*" or token1 == "/") and (token2 == "+" or token2 == "-")

def is_operator(s, pos):
    char = s[pos]
    #cases: -6, 4-5, 4- 5
    if pos + 1 < len(s):
        if char == '-':
            if s[pos + 1].isdecimal():
                if s[pos - 1].isdecimal(): # is operator
                    return True
                else:
                    return False
            else:
                return True
    if char == '+' or char == '/' or char == '*':
        return True

def get_output_queue(input_string):
    new_start_position = 0
    output_queue = []
    operator_stack = []
    while new_start_position < len(input_string):
        char = input_string[new_start_position]
        if char == ' ':
            new_start_position += 1
        elif is_operator(input_string, new_start_position):
            while len(operator_stack) != 0 and has_precedence(operator_stack[-1], char) and operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            operator_stack.append(char)
            new_start_position += 1
        elif char == '(':
            operator_stack.append(char)
            new_start_position += 1
        elif char == ')':
            while len(operator_stack) != 0 and operator_stack[-1] != '(':
                a = operator_stack.pop()
                output_queue.append(a)
            if len(operator_stack) != 0 and operator_stack[-1] == '(':
                operator_stack.pop()
            new_start_position += 1
        else:  # build decimal string
            digits = []
            if char == '-' and (new_start_position + 1 < len(input_string)) and input_string[new_start_position + 1].isdecimal():  # if negative number
                digits.append(char)
                new_start_position += 1
                char = input_string[new_start_position]
            while char.isdecimal() and new_start_position < len(input_string):
                digits.append(char)
                new_start_position += 1
                if new_start_position == len(input_string):
                    digit_string = "".join(digits), new_start_position
                    break
                char = input_string[new_start_position]
            digit_string = "".join(digits)
            output_queue.append(digit_string)
    while len(operator_stack) > 0:
        output_queue.append(operator_stack.pop())
    return output_queue

def calculate(s):
    answer = []
    for i, token in enumerate(s):
        if token == '+' or (token == '-' and len(token) == 1) or token == '*' or token == '/':
            b = answer.pop()
            a = answer.pop()
            c = eval('a' + token + 'b')
            answer.append(c)
        else:
            answer.append(Fraction(token))
    return answer[0]


out_q = get_output_queue(s)
ans = calculate(out_q)


