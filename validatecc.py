def validatecc(num):
	'''Validate a credit card number; returns True or False'''
	num = num if type(num) is str else str(num)
	if len(num) != 16: return False
	try:
		digits = [int(char) for char in num]
	except ValueError: return False
	total = 0
	for i in range(0,15,2): # for every pair of digits
		x = digits[i]*2 # first digit of pair * 2
		x = x if x < 10 else x-10+1 # if result is double-digit, sum up its digits
		total += x + digits[i+1] # add second digit of pair
	return total%10 == 0 # true if divisible by 10

if __name__=='__main__':
	print('Valid!' if validatecc(input('Enter 16-digit credit card number: ').strip()) else 'Invalid!')
	input()