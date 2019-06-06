for num in range(1,101):
	if num%7==0 or num%10==7 or (num>69 and num< 80):
		continue
	else:
		print(num)
