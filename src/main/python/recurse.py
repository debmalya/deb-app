def recurse(i,n=0):
	if (n<=50):
		print(n)
		recurse(n+n,i*i)
	else:
		print(n)
		
recurse(1)			
