import math
from decimal import Decimal
x_indexArray = []
y_indexArray = []
x_logArray = []
y_logArray = []
b_data = []
c_data = []
def convertData():
	datafile = open("data.txt","r")
	for data in datafile.readlines():
		data = data.strip("\n")
		rawData = [2]
		rawData = data.split()
		x_indexArray.append(rawData[0])
		y_indexArray.append(rawData[1])
def displayData():
	x = len(b_data)
	finalB = 0
	finalC = 0
	while (x > 0):
		finalB = finalB + b_data[x-1]
		finalC = finalC + c_data[x-1]	
		x=x-1
	finalB = finalB/len(b_data)
	finalC = finalC/len(b_data)
	print "Final function is Y = c*X^b"
	print "b = "+str(finalB)
	print "c = "+str(finalC)
def indexFinder():
	for data in x_indexArray:
		data = math.log10(Decimal(data))
		x_logArray.append(data)
	for data in y_indexArray:
		data = math.log10(Decimal(data))
		y_logArray.append(data)
	x = len(x_logArray)
	while (x > 1):
		b = (y_logArray[x-1]-y_logArray[x-2])/(x_logArray[x-1]-x_logArray[x-2])
		b_data.append(math.pow(10, b))
		c = y_logArray[x-1]-b*x_logArray[x-1]
		c_data.append(math.pow(10, c))
		x=x-1
def main():
	convertData()
	indexFinder()
	displayData()
if __name__ == "__main__":
	main()
