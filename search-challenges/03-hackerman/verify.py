import re, os

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

def hackfile(path) : 
    return os.path.dirname(os.path.abspath(__file__)) + "/" + path

text_file = open(hackfile("alice.txt"), "r")
data = text_file.read()
text_file.close()

message = "Great, you managed to find the find my notes. I can finally speak freely now that nobody can overhear. Your first step will be to find the access server. I wrote it down in my notes somewhere. It should not be too hard to find. We want to find the server's ip address. This is a sequence of 3 numbers, between 0 and 255. This is repeated 4 times, separated by dots. An example would be '129.178.255.211'"

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
print(raw_solutions)

regex_pattern = re.compile("(< ).+")
print("foo")
print(regex_pattern.match("< foo"))
print(regex_pattern.match('> [0-9]{1-3}.[0-9]{1-3}.[0-9]{1-3}.[0-9]{1-3}\n'))
print("bar")

solutions =  list(map(lambda x : re.match(x, "< (.+)"), raw_solutions))
print(solutions)
print(list(solutions))
