
def process(inputs):
	"""
	To process the inputs and generate seating arrangements.
	"""
	values=inputs[0].split()
	number_of_seats=int(values[0])
	number_of_scientists=int(values[1])
	first_taken_seat=inputs[1]
	checking=inputs[2]
	checked_seats=inputs[3]
	occupied=[False] * number_of_seats
	occupied[first_taken_seat-1]=True
	return inputs[3]


# take number of test cases.
number_of_test_cases=int(raw_input(""))

outputs=[]
# now take input for each test case
for x in range(number_of_test_cases):
	inputs=[]
	# number of seats number of scientists
	inputs.append(raw_input(""))
	# index of first taken seat
	inputs.append(int(raw_input("")))
	# number of scientists whose seat we want to check
	inputs.append(int(raw_input("")))
	# indexes of the scientists in ascending order
	inputs.append(raw_input(""))
	outputs.append(process(inputs))

# print output for each test case
for x in range(number_of_test_cases):
	# To print the final output	
	print outputs[x] 
