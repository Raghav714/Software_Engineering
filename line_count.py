#reading the file 
f= open("gaurav.c")
lines = f.read()
#list contain the symbol which represent the end of line
lis = ["h> ","()","{","}",";","if","else"]
'''counting the source code line
for example void main() { 
this is considered the two separate line contributing for the number of source code line''' 
no_l = 0
for l in lis:
	no_l = no_l + lines.count(l)
print "source code",no_l
#counting the single line comment
sl=lines.count("//")
#counting the number of balank lines and mutilple comments
print "single line comment",sl
# bl has been assigned to -1 because the file always end with the blank line at last
bl = -1
#the code is split depending upon the new line and put into the list
lines = lines.split("\n")
#index consist of the line number where the multiple line comment start and end 
index = []
#flag is used to denote the line number
flag = 0
for line in lines:
	flag = flag+1
	# this segment is used to count the blank lines in the code
	if line =='':
		bl = bl+1
	# this segment is used to find the line number where the muti-line comment start and end
	if "*" in line:
		index.append(flag)
#find the line of string
mul = index[1]-index[0]+1
print "multi line comment",mul
print "blank lines",bl
'''summation of number of source code line ,muti-line comment,blank line and single line comment
is physical number of line'''
print "LOC",bl+mul+sl+no_l
