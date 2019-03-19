import sys
from math import log

if(len(sys.argv) != 2):
    print("error")
    exit()
programFileName = sys.argv[1]

op = ["main","scanf","printf","print","(","{","[",")","}","]","+","-","*","<",">","<=",">=","for","while","do","if","else","return","=","==","byte","char","short","int","long","float","double"]
operators = {}
operands = {}

for f in op:
	operators[f.replace('\n','')] = 0

isAllowed = True

with open(programFileName) as f:
    for line in f:
        line = line.strip("\n").strip(' ')

        if(line.startswith("/*")):
            isAllowed = False
       
        if((not line.startswith("//")) and isAllowed == True and (not line.startswith('#'))):
            for key in operators.keys():
                operators[key] = operators[key] + line.count(key)
                line = line.replace(key,' ')
            for key in line.split():
                if key in operands:
                    operands[key] = operands[key] + 1
                else:
                    operands[key] = 1

        if(line.endswith("*/")):
            isAllowed = True


n1, N1, n2, N2 = 0, 0, 0, 0

print("OPERATORS:\n")
for key in operators:
    if(operators[key] > 0):
        if(key not in ")}]"):
            n1, N1 = n1 + 1, N1 + operators[key]
            print(key, operators[key])

print("\nOPERANDS\n")
for key in operands.keys():
    if(operands[key] > 0):
        n2, N2 = n2 + 1, N2 + operands[key]
        print(key, operands[key])

print "Volume ",(N1+N2) * log (n1+n2)
#Formula: (N1+N2) * log2 (n1+n2)
print "difficulty",(n1/2) * (N2/n2)
#Formula: (n1/2) * (N2/n2)
