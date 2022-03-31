"""
Write the code in order to solve the problem below;
minusthreemultiplyfivedividezeropointfiveplusten
"""
quest1 = "minusthreemultiplyfivedividezeropointfiveplusten"
dict_strToDigits = {
	"zero" :0,
	"one" :1,
	"two":2,
	"three":3,
	"four":4,
	"five":5,
	"six":6,
	"seven":7,
	"eight":8,
	"nine":9,
	"ten":10,
	"minus":"-",
	"plus":"-",
	"multiply":"*",
	"divide":"/",
	"point":"."}

def calculator(input):
	#minus en son operator olarak sorgulanmalı yoksa yanlış split eder
	for i in dict_strToDigits:
		input = str(input.replace(i, str(dict_strToDigits.get(i))))
	print(input," = ", eval(input))
	return eval(input)

calculator(quest1)
