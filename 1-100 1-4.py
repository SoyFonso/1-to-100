import itertools
import math

number = int(input('Selecciona un número. '))
numbers = [1, 2, 3, 4]
operators = ["", "*", "+", "-", "**", '/']
for a, b, c, d in itertools.permutations(numbers):
    for op1, op2, op3 in itertools.combinations_with_replacement(operators, 3):
        result = f'{a}{op1}{b}{op2}{c}{op3}{d}'
        if eval(result) == number:
            print(f'{eval(result)} = {result}')

numbers2 = [1, 2, math.factorial(3), math.factorial(4)]
operators2 = ["", "*", "+", "-", '/']

for a, b, c, d in itertools.permutations(numbers2):
    for op1, op2, op3 in itertools.combinations_with_replacement(operators2, 3):

        result = f'{a}{op1}{b}{op2}{c}{op3}{d}'
        result2 = f'{a}{op1}{b}{op2}({c}{op3}{d})'
        result3 = f'{a}{op1}({b}{op2}{c}){op3}{d}'
        result4 = f'({a}{op1}{b}){op2}{c}{op3}{d}'
        result5 = f'({a}{op1}{b}{op2}{c}){op3}{d}'
        result6 = f'{a}{op1}({b}{op2}{c}{op3}{d})'
        result7 = f'({a}{op1}{b}){op2}({c}{op3}{d})'

        if eval(result) == number:
            print(f'{eval(result)} = {result}')

        elif op2 != "":
            if eval(result2) == number:
                print(f'{eval(result2)} = {result2}')
            if eval(result4) == number:
                print(f'{eval(result4)} = {result4}')

        elif op3 and op1 != "":
            if eval(result3) == number:
                print(f'{eval(result3)} = {result3}')

        elif op3 != "":
            if eval(result5) == number:
                print(f'{eval(result5)} = {result5}')

        elif op1 != "":
            if eval(result6) == number:
                print(f'{eval(result6)}= {result6}')

        elif op2 != "":
            if eval(result7) == number:
                print(f'{eval(result7)} = {result7}')

for a, b, c, d in itertools.permutations(numbers):
    for op1, op2, op3 in itertools.combinations_with_replacement(operators, 3):

        result = f'{a}{op1}{b}{op2}{c}{op3}{d}'
        result2 = f'{a}{op1}{b}{op2}({c}{op3}{d})'
        result3 = f'{a}{op1}({b}{op2}{c}){op3}{d}'
        result4 = f'({a}{op1}{b}){op2}{c}{op3}{d}'
        result5 = f'({a}{op1}{b}{op2}{c}){op3}{d}'
        result6 = f'{a}{op1}({b}{op2}{c}{op3}{d})'
        result7 = f'({a}{op1}{b}){op2}({c}{op3}{d})'

        if eval(result) == number:
            print(f'{eval(result)} = {result}')

        elif op2 != "":
            if eval(result2) == number:
                print(f'{eval(result2)} = {result2}')
            if eval(result4) == number:
                print(f'{eval(result4)} = {result4}')

        elif op3 and op1 != "":
            if eval(result3) == number:
                print(f'{eval(result3)} = {result3}')

        elif op3 != "":
            if eval(result5) == number:
                print(f'{eval(result5)} = {result5}')

        elif op1 != "":
            if eval(result6) == number:
                print(f'{eval(result6)}= {result6}')

        elif op2 != "":
            if eval(result7) == number:
                print(f'{eval(result7)} = {result7}')

numbers3 = [1, 2, 3, math.factorial(4)]
operators3 = ["", "*", "+", "-", '/']
for a, b, c, d in itertools.permutations(numbers3):
    for op1, op2, op3 in itertools.combinations_with_replacement(operators3, 3):
        result = f'{a}{op1}{b}{op2}{c}{op3}{d}'
        result2 = f'{a}{op1}{b}{op2}({c}{op3}{d})'
        result3 = f'{a}{op1}({b}{op2}{c}){op3}{d}'
        result4 = f'({a}{op1}{b}){op2}{c}{op3}{d}'
        result5 = f'({a}{op1}{b}{op2}{c}){op3}{d}'
        result6 = f'{a}{op1}({b}{op2}{c}{op3}{d})'
        result7 = f'({a}{op1}{b}){op2}({c}{op3}{d})'

        if eval(result) == number:
            print(f'{eval(result)} = {result}')

        elif op2 != "":
            if eval(result2) == number:
                print(f'{eval(result2)} = {result2}')
            if eval(result4) == number:
                print(f'{eval(result4)} = {result4}')

        elif op3 and op1 != "":
            if eval(result3) == number:
                print(f'{eval(result3)} = {result3}')

        elif op3 != "":
            if eval(result5) == number:
                print(f'{eval(result5)} = {result5}')

        elif op1 != "":
            if eval(result6) == number:
                print(f'{eval(result6)}= {result6}')

        elif op2 != "":
            if eval(result7) == number:
                print(f'{eval(result7)} = {result7}')


numbers4 = [1, 2, math.factorial(3), 4]
operators4 = ["", "*", "+", "-", '/']
for a, b, c, d in itertools.permutations(numbers4):
    for op1, op2, op3 in itertools.combinations_with_replacement(operators4, 3):
        result = f'{a}{op1}{b}{op2}{c}{op3}{d}'
        result2 = f'{a}{op1}{b}{op2}({c}{op3}{d})'
        result3 = f'{a}{op1}({b}{op2}{c}){op3}{d}'
        result4 = f'({a}{op1}{b}){op2}{c}{op3}{d}'
        result5 = f'({a}{op1}{b}{op2}{c}){op3}{d}'
        result6 = f'{a}{op1}({b}{op2}{c}{op3}{d})'
        result7 = f'({a}{op1}{b}){op2}({c}{op3}{d})'

        if eval(result) == number:
            print(f'{eval(result)} = {result}')

        elif op2 != "":
            if eval(result2) == number:
                print(f'{eval(result2)} = {result2}')
            if eval(result4) == number:
                print(f'{eval(result4)} = {result4}')

        elif op3 and op1 != "":
            if eval(result3) == number:
                print(f'{eval(result3)} = {result3}')

        elif op3 != "":
            if eval(result5) == number:
                print(f'{eval(result5)} = {result5}')

        elif op1 != "":
            if eval(result6) == number:
                print(f'{eval(result6)}= {result6}')

        elif op2 != "":
            if eval(result7) == number:
                print(f'{eval(result7)} = {result7}')