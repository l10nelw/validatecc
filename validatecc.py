def validatecc(num):
	'''Validate a credit card number; returns True or False'''
	num = num if type(num) is str else str(num)
	digits = [int(char) for char in num]
	if len(digits) != 16: return False
	sum = 0
	for i in range(0,15,2): # every pair of digits
		x = digits[i]*2 # first digit * 2
		x = x if x < 10 else x-10+1 # if x is double-digit, sum up the digits
		sum += x + digits[i+1] # add second digit
	return sum%10 == 0 # true if divisible by 10

if __name__=='__main__':
	print('Valid!' if validatecc(input('Enter 16-digit credit card number: ').strip()) else 'Invalid!')