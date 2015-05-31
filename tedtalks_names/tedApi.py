import httplib
import requests
import os
import random
from time import sleep

#http://api.ted.com/v1/talks.json?api-key=r7b7vtktewzmjs29dwuvvrtk&filter=id:1300
l1 = r'http://api.ted.com/v1/talks.json?api-key=r7b7vtktewzmjs29dwuvvrtk&filter=id:'
#l2 = r'/subtitles.json?api-key=r7b7vtktewzmjs29dwuvvrtk' 
writeError = open('missedFiles.txt','a')
for i in range(1,2300):
	f1 ='name' + str(i) + ".txt"
	writeFile = open(f1,'w')
	lFinal = l1 + str(i)
	try:
		r = requests.get(lFinal)
		writeFile.write(r.text)
		print "Finished writing file:" + str(i)
		writeFile.close()
	except :
		#sleep(random.randrange(0,5))
		writeFile.close()
		print "Missed this file \n"
		temp = str(i) + '\n'
		writeError.write(temp)
		continue

	#short_rand = random.randrange(0,5) / 10.0
	#print short_rand
	#sleep(short_rand)



