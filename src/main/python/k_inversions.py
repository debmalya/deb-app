def get_no_of_inversions(n,k):
	if k == 0 or k == n:
		print(1)
	elif k == 1:
		print(n - 1)	
	
	
no_of_test_cases = int(raw_input())
inputs=[]
for i in range(no_of_test_cases):
	inputs.append(raw_input())
	
for i in range(no_of_test_cases):
	values=inputs[i].split(" ")	
	n=int(values[0])
	k=int(values[1])
	get_no_of_inversions(n,k)
