import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
text_file = open("alice.txt", "r")
data = text_file.read()
text_file.close()

message = "Great, you managed to find the find my notes. I can finally speak freely now that nobody can overhear. Your first step will be to find the access server. I wrote it down in my notes somewhere. It should be too hard to find. We want to find to find the server's ip address a sequence of 3 numbers, between 0 and 255. This is repeated 4 times, separated by dots. An example would be '129.178.255.211"

for i, c in enumerate(message):
  #  print((bcolors.OKBLUE, bcolors.OKCYAN,bcolors.OKGREEN)[i%3], end="")
    print(c, end="")

print("")
solution_file = open("solution.txt", "r")
raw_solutions = solution_file.readlines()
solution_file.close()

foo = [1,2,3]
bar =  map(lambda x:x*x, foo)

for x in bar:
    print(x)
#solutions =  raw_solutions[re.match(x, "< ?(.+)") for x in range(len(raw_solutions))]
#print(solutions)
