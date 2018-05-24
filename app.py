import sys, time, json, requests
from random import randint

params = sys.argv[1]
print("-------------------------" + params)
data_json = json.loads(params)
with open("./log", "a") as myfile:
	myfile.write(str(data_json) + "\n")
	print(data_json)
	#d = randint(10, 60)
	d = int(data_json['sleep'])
	server = data_json['server']
	id = data_json['id']
	for x in range(0,d):
		log = {'id': data_json['id'], 'current_index': x, 'total':d}
		local_url =  server + "/experiment/result" 
		requests.post(local_url, json= log)
		time.sleep(1)

	'''
	myfile.write("------- Waiting for " + str(d) + "------" + "\n")
	print("------- Waiting for " + str(d) + "------")
	time.sleep(d)
	myfile.write("------- Finished ------" + "\n")
	print("--------- Finished ----------------")
	'''

	
sys.exit(0)