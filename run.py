import time, shlex, subprocess, random

command = ['docker','exec', '1d51bd76ac12'] + ['python3', 'app.py', '{"id": "id_1","sleep": "10", "misc": ["127.0.0.252"]}']
output = subprocess.check_output(command)
print(output)

