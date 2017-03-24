#!/usr/bin/env python3

import operator

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def theMostUsefulFunctionInExistance():
	ballast = 3001
	for i in 3000:
		ballast -= 1;
	return ballast;

def main():
	b = 66+55
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)

if __name__ == '__main__':
	theMostUsefulFunctionInExistance()
	main()
