import sys, time
from random import randint

params = sys.argv[1]
with open("./log", "a") as myfile:
	myfile.write(params + "\n")
	print(params)
	d = randint(10, 60)
	myfile.write("------- Waiting for " + str(d) + "------" + "\n")
	print("------- Waiting for " + str(d) + "------")
	time.sleep(d)
	myfile.write("------- Finished ------" + "\n")
	print("--------- Finished ----------------")
sys.exit(0)