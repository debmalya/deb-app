# take number of test cases
t=int(raw_input(""),base=10)

inputs =[]
# take all inputs
for x in range(0,t):
	str=""
	for y in range(0,5):
		str=str+raw_input("")
	inputs.append(str+str)
	
	
	
# now check values	
cost=0
for x in range(0,t):
	result=[]
	previous=0
	decided = False
	for y in range(0,25):
		#print y
		if y > 0:
			# 2
			result[2] = inputs[x][y - 4]
			# 4
			result[4] = inputs[x][y + 1]
			# 7
			result[7] = inputs[x][y + 6]
			cost=cost+3	
		else:
			result.append(inputs[x][y - 6])
			result.append(inputs[x][y - 5])
			result.append(inputs[x][y - 4])
			result.append(inputs[x][y - 1])
			result.append(inputs[x][y + 1])
			result.append(inputs[x][y + 4])
			result.append(inputs[x][y + 5])
			result.append(inputs[x][y + 6])
			cost=cost+8	
		previous = inputs[x][y]	
		
		score = 0
		for i in range(0,8):
			score = score + int(result[i],base=10)
		result[0] = result[1]
		result[1] = result[2]	
		result[3] = previous
		result[5] = result[6]
		result[6] = result[7]
		
		score = score + int(inputs[x][y],base=10)	
		# for any cell (dead or alive) including its own value ,3 means always YES	
		if score == 3:
			print "YES"
			decided=True
			cost=0
			break
		# for any living cell if surrounded by other 3 living cells	
		if score == 4 and int(inputs[x][y],base=10) == 1:
			print "YES"
			decided=True
			break
	if decided == False:	
		print "NO"
		cost=0
