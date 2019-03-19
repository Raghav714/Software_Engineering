class CSStudent: 
	stream = 'cse'
	year = '2016'
	col = 'IIITM' 
	def __init__(self, roll): 
		self.roll = roll
          
	def setAddress(self, address): 
	        self.address = address
		print "setadd",self.stream,self.year,self.col

	def getAddress(self):
		print "getadd",self.stream,self.col
		return self.address    

a = CSStudent(101) 
a.setAddress("Noida, UP") 
print(a.getAddress())  
