#is_debug=True
is_debug=False

def process_input(test_string):
    # this method will process input
    values=test_string.split("j")
    first_number=complex(0,0)
    second_number=complex(0,0)
    result=complex(0,0)
    for each in values:
        real_value=each.strip()
                
        if len(real_value)>0:
            operator=real_value[0]
            #check whether first character of real value is an operator or not
            if operator.isdigit():
                #does not start with operator.
                first_number = get_number(real_value)
            else:
                #operator onward string passed to get_number to get the complex number
                second_number = get_number(real_value[1:])
                try:
                    if operator=='+':
                                        result=first_number+second_number
                    elif operator=='-':
                                            result=first_number-second_number
                    elif operator=='*':
                                            result=first_number-second_number
                    elif operator=='/':
                                            
                                            result=first_number/second_number
                    if is_debug:
                                            print str(first_number) + operator + str(second_number) + " = " + str(result)
                    first_number=result
                except ZeroDivisionError:
                                    print "Zeroes are not heroes. Do not try them as divisor."
                except TypeError:
                                    print "Supports only complex number. Sorry"
                                    return None
    if is_debug:
        print "Result       :" + str(result)
    return first_number


def get_number(value):
    # Create a complex number from the passed value.
    # value is expected in the format m+nj (complex) 
    # whatever comes before + is the real part.
    # whatever comes after + is the imaginary part.
    if is_debug:
        print "method : get_number, passed value :" + value
    all_values=value.split("+")
    number_of_elements=len(all_values)
    if number_of_elements == 2:
        c=complex(float(all_values[0]),float(all_values[1]))
        if is_debug:
                print c
        return c

def test():	
    test_string="3+5j -1+2j+1+4j *4+3j"
    print process_input(test_string)
    test_string="3+5"
    print process_input(test_string)

prompt="Enter expression: "
test_string=raw_input(prompt)	
print process_input(test_string)



