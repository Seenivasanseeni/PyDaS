import sys
file=open(sys.argv[1])
file2=open(sys.argv[1]+"-copy","w")
s=file.readline()
while(s!=''):
	s=s.strip()
	s=s+"\n"
	print(s)
	file2.write(s)
	s=file.readline()
file2.close()
file.close()

