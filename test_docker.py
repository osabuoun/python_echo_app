from __future__ import absolute_import, unicode_literals
import time, shlex, subprocess, random

command = ['docker','exec', "no_container"] + ["python3", "app.py" , "test"]

try:
	output = subprocess.check_output(command)
except subprocess.CalledProcessError as e:
	print("This is an error")
except Exception as ex:
	raise ex
