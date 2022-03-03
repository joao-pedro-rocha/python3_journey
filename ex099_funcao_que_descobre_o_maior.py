def maior(*numero):
	mai = c = 0
	
	for n in numero:
		c += 1
		
		if c == 1:
			mai = n
	
		else:
			if n > mai:
				mai = n
		
	print(mai)


maior(9, 155, 12)
