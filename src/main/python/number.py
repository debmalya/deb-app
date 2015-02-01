class my_calculator(object):
    def __init__(self,expression):
        self.expression=expression

    def do_operation(self):
        # parse expression
        num1_str=""
        num2_str=""
        num1=my_number()
        num2=my_number()
        operand_found=False
        
        for letter in self.expression:
            # if the leter is not an operand +,-,*,/
            if letter == '+' or letter == '-' or letter == '*' or letter == '/':
                operand_found=True
                #elif letter == 'j':
                # it is imaginary part

                # then it is a number.



class my_number(object):
    

    def set_real(self,real):
        # to set the real part
        self.real=real
    
    def set_imag(self,imag):
        # to set the imaginary part
        self.imag=imag
	
    def add(self,num2):
		r = complex(self.real,self.imag)+complex(num2.real,num2.imag)
		if r.imag == 0:
			#real number
			return r.real
		return r

    def subtraction(self,num2):
        r = complex(self.real,self.imag)-complex(num2.real,num2.imag)
        if r.imag == 0:
            #real number
            return r.real
        return r

    def multiplication(self,num2):
        r = complex(self.real,self.imag)*complex(num2.real,num2.imag)
        if r.imag == 0:
            #real number
            return r.real
        return r

    def division(self,num2):
        try:
            r = complex(self.real,self.imag)/complex(num2.real,num2.imag)
            if r.imag == 0:
                #real number
                return r.real
            return r
        except ZeroDivisionError:
            print "Can not divide by zero"








def test():
    print "Test"
    num1=my_number()
    test_string="3+5j -1+2j+1+4j *4+3j"
# main program
test()
print "All things bright and beautiful"

