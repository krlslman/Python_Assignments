import string

letter_lib = {}
#user_input = input("Enter the text you want to analyze : )
user_input = """If you want to succeed something, you can succeed it with these two rules: 
			1) Want it so bad 
			2) Have a good plan"""  
alphabet = set(string.ascii_letters)
# alphabet.
for i in alphabet:
	a = user_input.count(i)
	if int(a) > 0:
		letter_lib[i] = a

for keys,value in letter_lib.items():
  print("-Letter",keys,"is repeated",value, "time(s)")
