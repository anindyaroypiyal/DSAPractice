def makeBeautiful(str):
	# Write your code here
	for0 = pattern(str, '0')

	for1 = pattern(str, '1')
	
	return (min(for0,for1)) 



def pattern(str, case):
	prev = case

	if (str[0] == '0') and (prev == '1'):
		operations = 1
	elif (str[0] == '1') and (prev == '0'):
		operations = 1
	else:
		operations = 0

	for i in range(1,len(str)):
		if prev == '0':
			if str[i] == '0':
				operations += 1
				prev = '1'
			else:
				prev = str[i]
		else:
			if str[i] == '1':
				operations += 1
				prev = '0'
			else:
				prev = str[i]

	return operations