import math
def process(inputs):
	for input in inputs:
		values=input.split()
		count=0
		ab=0
		ac=0
		ad=0
		bc=0
		bd=0
		cd=0
		vol=0
		for value in values:
			count=count+1
			if count==1:
				ab=int(value)
			elif count==2:
				ac=int(value)
			elif count==3:
				ad=int(value)
			elif count==4:
				bc=int(value)
			elif count==5:
				bd=int(value)
			elif count==6:
				cd=int(value)
			if count==6:
				if ab==ac and ab==bc:
					vol=(math.sqrt(2)/12)*ab*ab*ab
				else:
					u=(bd*bd+cd*cd)-(bc*bc)
					v=(cd*cd+ad*ad)-(ac*ac)
					w=(ad*ad+bd*bd)-(ab*ab)
					vol=(math.sqrt(4*(ad*ad*bd*bd*cd*cd)-(ad*ad*u*u)-(bd*bd*v*v)-(cd*cd*w*w)+(u*v*w)))/12
				print round(vol,4)
				
number_of_test_cases=int(raw_input(""),base=10)

inputs=[]
for x in range(number_of_test_cases):
	inputs.append(raw_input(""))

process(inputs)
