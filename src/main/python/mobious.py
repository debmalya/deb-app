import math

def isPrime(n,p):
    if n < 2: return False
    l=2
    print(str(p))
    for i in p:
		if n%i==0:
			return False
		l=i	
    for i in range(l,int(math.sqrt(n))):
    	if n%i==0:
    		return False
    return True		
    		
	
def mobious(N):
	i = 2
	prime=[]
	N=long(N)
	while i <= N/2:
		isP = False
		if N%i==0:
			try:
   				b=prime.index(i)
   				isP = True
			except ValueError:
				if isPrime(i,prime)==True:
					prime.append(i)
					
    				isP = True
    		if isP:
    			if N%(i*i)==0:
    				print(0)
    		i+=1			
	#print("primes :"+str(prime))						
	print((-1)**len(prime))

#print(isPrime(2,()))
# print(isPrime(10,(2,5)))
# print(isPrime(21,()))
# mobious("10")
#mobious("7")
#mobious("18")
#mobious("21")
# mobious("42")
#mobious("9")
