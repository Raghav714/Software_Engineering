import sys
class doc_type:
	def __init__(self,lines):
		self.lines = lines
	def cls_var_count(self):#calculating the class variable
		count =len(self.fn_name())
		return count
	def cls_var(self):#finding the class variable
		var = []
		for line in self.lines:
			if "=" in line:
				var.append(line[0:line.find("=")])
			elif "def" in line:
				break
		return var
	def fn_name(self):#finding the function name
		name = {}
		for index in range(len(self.lines)):
			if "def" in self.lines[index]:
				name[index] = self.lines[index][self.lines[index].find(" "):self.lines[index].find("(")]
		return name	
	def fn_var(self):#finding the variable used in function
		dic = {}
		var = self.cls_var()
		names = self.fn_name()
		keys = sorted(names.keys())
		keys.append(len(self.lines))
		for i in range(len(keys)):
			if keys[i] == len(self.lines):
				break
			for va in var:
				count = 0
				vari = va.strip()
				for index in range(keys[i],keys[i+1]):
					#print va,self.lines[index]
					if vari in self.lines[index]:
						print vari,"		|	",names[keys[i]]
if __name__== "__main__": #driver class
	fl_na = sys.argv[1]
	f= open(fl_na)
	lines = f.read().split("\n")
	d = doc_type(lines)
	print "class variable",d.cls_var()
	print "function name",d.fn_name().values()
	print "variable	|	function"
	d.fn_var()
