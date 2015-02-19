try:
	score=float(raw_input("Enter score[0.0-1.0]"))
	if score >=0.9 and score <= 1.0:
		print "A"
	elif score >=0.8 and score < 0.9:
		print "B"
	elif score >=0.7 and score < 0.8:
		print "C"
	elif score >=0.6 and score < 0.7:
		print "D"
	elif score <0.6 and score >= 0:
		print "F"
	else: 
		print "Out of range"
except ValueError:
	print "Invalid input. Must be float [0.0 - 1.0]."			
	
			
	
	
