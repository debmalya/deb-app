"""
Write a program to read through the mbox-short.txt and 
figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop 
to find the most prolific committer.
"""
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
senders = dict()
for line in fh:
    if len(line) > 0 and line.startswith("From "):
        word=line.split()[1]
        senders[word] = senders.get(word,0)+1
        
maxCount = None
maxSender = None
for sender,count in senders.items():
	if maxCount is None or count > maxCount:
		maxSender = sender
		maxCount = count

print maxSender, maxCount
