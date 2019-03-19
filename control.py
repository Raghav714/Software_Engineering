import sys
class assign3:
	def __init__(self,pointer,lines):
		self.pointer = pointer
		self.lines = lines
	def cond_pre(self):
		count = 0
		for item in [x for x in self.lines if x]:
			if "#" == item[0]:
				count+=1
		return count
	def ter(self):
		count = 0
		for item in [x for x in self.lines if x]:
			if "?" in item and ":" in item:
				count+=1
		return count
	def try_catch(self):
		count = 0
		for item in [x for x in self.lines if x]:
			if "catch" in item:
				count+=1
		return count
	def cond(self):
		count = 0
		for element in ["if","elseif","elif","else"]:
			for item in [x for x in self.lines if x]:
				if element in item:
					count+=1
		return count
	def loop(self):
		count = 0
		for element in ["for","foreach","switch"]:
			for item in [x for x in self.lines if x]:
				if element in item:
					count+=1
		return count
	def case(self):
		count = 0
		while self.lines[self.pointer]:
			#print self.lines[self.pointer]
			if "case" in self.lines[self.pointer] and "case" in self.lines[self.pointer+1]:
				count+=1
				self.pointer+=2
				continue
			self.pointer+=1
		return count
fl_na = sys.argv[1]
f= open(fl_na)
lines = f.read()
lines = lines.split("\n")
parser = assign3(0,lines)
print parser.cond_pre()
print parser.ter()
print parser.try_catch()
print parser.cond()
print parser.loop()
print parser.case()
