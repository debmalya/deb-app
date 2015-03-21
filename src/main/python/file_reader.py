"""
Open the file. Read it line by line. 
For each line, split the line into a list of words using the split() function. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
"""
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	words=line.split()
	for each_word in words:
		if each_word not in lst:
			
			lst.append(each_word)
lst.sort()			
print(lst)			
					
