def line_count(code):
	#list contain the symbol which represent the end of line
	lis = ["h> ","()","{","}",";","if","else"]
	'''counting the source code line
	for example void main() { 
	this is considered the two separate line contributing for the number of source code line''' 
	no_l = 0
	for l in lis:
		no_l = no_l + lines.count(l)
	result = "source code" + str(no_l)
	#counting the single line comment
	sl=lines.count("//")
	#counting the number of balank lines and mutilple comments
	result = result + "single line comment" + str(sl)
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
	result = result + "multi line comment" + str(mul)
	result = result + "blank lines"+str(bl)
	'''summation of number of source code line ,muti-line comment,blank line and single line comment is physical number of line'''
	result = result + "LOC"+ str(bl+mul+sl+no_l)
	return result
