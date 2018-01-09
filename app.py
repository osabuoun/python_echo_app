import sys, time, json
from random import randint

params = sys.argv[1]
print("-------------------------" +params)
data_json = json.loads(params)
with open("./log", "a") as myfile:
	myfile.write(str(data_json) + "\n")
	print(data_json)
	#d = randint(10, 60)
	d = int(data_json['sleep'])
	server = data_json['server']
	myfile.write("------- Waiting for " + str(d) + "------" + "\n")
	print("------- Waiting for " + str(d) + "------")
	time.sleep(d)
	myfile.write("------- Finished ------" + "\n")
	print("--------- Finished ----------------")
	'''
	local_url =  server + "/api/v1/query?query=" + query
	try:
		return requests.post(local_url).json()
	except Exception as e:
		return {"status": "failed", "message":e}
	'''
sys.exit(0)