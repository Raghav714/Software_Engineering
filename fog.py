import sys #to take the argument from user
class doc_type:
	def __init__(self,lines):
		self.lines = lines #constructor to assign the file data
	def words(self):#this function will return count of the total number of word and unique word
		return len(self.lines),set(self.lines)
	def no_sent(self): #this will return the number of sentence
		count = 0
		sen_ter = [".","?","!"]
		for ter in sen_ter:
			for word in self.lines:
				if ter in word:
					count+=1
		return count		
	def syl(self): #this will count the number of syllables with diphthongs attention
		syal = []
		count = 0
		no_com = 0
		vow = ["a","e","i","o","u"]
		for word in self.lines:
			flag = count
			for i in range(0,len(word)-1):#the last vowel is not taken in consideration
				for v in vow:
					if v == word[i] and v!=word[i+1]:
						count+=1
			if count-flag > 2:
				no_com+=1
		return count,no_com
		
	def fog(self): #this will count the Fog's index 
		return 0.4*(self.words()[0]/self.no_sent())+100*(self.syl()[1]/self.words()[0])
if __name__== "__main__":
	fl_na = sys.argv[1]
	f= open(fl_na)
	lines = f.read().split(" ")
	doc = doc_type(lines) #this will create a object of doc_type class
	print "words",doc.words() #this will call the function word()
	print "no of sen",doc.no_sent() #this will call the function no_sent()
	print "no of syll and complex word",doc.syl() #this will call the function syl() 
	print "fog index", doc.fog() #this will call the function that calculate the Fog's index
'''0.4 *[(words/sentences) + 100 (complex words/words)]'''#formula used to calculate Fog's Index
