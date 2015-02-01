def factorial(n):
    if  n < 2:
        return 1
    else:
          return n * factorial(n - 1)
# take number of test cases
number_of_test_cases=int(raw_input(""),base=10)



outputs=[]
# take inputs for all test cases
for x in range(number_of_test_cases):	
	outputs.append(factorial(int(raw_input(""),base=10)))
	
	

for x in range(number_of_test_cases):
	print int(outputs[x])
	
