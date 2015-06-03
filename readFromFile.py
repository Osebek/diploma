def readResolutions(filename):
	resolucije = open("peaks.txt",'r')
	tabelaResolucij = []
	for line in resolucije:
		vrstica = line.split(";")
		vrstica[2] = vrstica[2].rstrip("\n")
		tabelaResolucij.append(vrstica)
	
	return tabelaResolucij

def getKey(item):
    return int(item[2])


def printRes(res):
	for a in res:
		print a[0] + " " + a[1] + " " + a[2]

resolutions = readResolutions('peaksred-on-maroon-mural.txt')
resolutions = sorted(resolutions, key=getKey)
printRes(resolutions)