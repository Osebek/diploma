import math
from decimal import *
def average(array):
	sum = 0
	for val in array:
		sum += float(array)

	return sum / (len(array) - 1)


def statTest(prveZnacilnice,drugeZnacilnice):

	razlika = []
	vsotaPrve = 0;
	vsotaRazlik = 0
	vsotaKvadratovRazlik = 0
	n = len(prveZnacilnice) - 1 
	for i in range(1, len(prveZnacilnice)):
		if i != len(prveZnacilnice)-1: 
			vsotaPrve += Decimal(prveZnacilnice[i])
			razlika.append(Decimal(prveZnacilnice[i]) - Decimal(drugeZnacilnice[i]))
			vsotaRazlik += razlika[-1]
		else:
			vsotaPrve += Decimal(prveZnacilnice[i].rstrip()[:-1])
			razlika.append(Decimal(prveZnacilnice[i].rstrip()[:-1]) - Decimal(drugeZnacilnice[i].rstrip()[:-1]))

			vsotaRazlik += razlika[-1]
	# "razlike so kul, seprav X-Y je gud"
	#print "razlike" + str(razlika)
	# vsota razlik je tud kul
	vsotaRazlik /= n		
	for r in razlika:
		vsotaKvadratovRazlik += math.pow(r - vsotaRazlik,2)

	s = Decimal(math.sqrt(vsotaKvadratovRazlik / (n-1)))
	Ttest = round((vsotaRazlik / s)*Decimal(round(math.sqrt(n),5)),5)
	print Ttest




znacilnice = []
for line in open("znacilnice.txt"):
	znacilnice.append(line)


for i in range(0,len(znacilnice)):
	znacilnice[i] = znacilnice[i].split(',')

#print znacilnice[25]
#print znacilnice[21]

statTest(znacilnice[21],znacilnice[0])


