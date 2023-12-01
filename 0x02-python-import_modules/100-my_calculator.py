#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculate(av, ac):
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(av[1])
    oper = av[2]
    b = int(av[3])

    if oper == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif oper == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif oper == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif oper == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    av = sys.argv
    ac = len(sys.argv)

    calculate(av, ac)
