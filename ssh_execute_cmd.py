import os
from dotenv import load_dotenv
import paramiko
import time

# Note : If you have active VPN or PROXY , It dose not work

# print(os.environ['HOME'])
# Use load_env to trace the path of .env:
load_dotenv('.env') 

# Get the values of the variables from .env using the os library:
host = os.environ.get("Host")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=host, username='ubuntu', key_filename='/home/ubuntu/keys/avid/pubnito-nightly.pem')

stdin, stdout, stderr = ssh.exec_command('sudo apt update')
print(stdout.readlines())
# The reason for the error (AttributeError: 'NoneType' object has no attribute 'time') is that the output print conflicts with the close executed by the program. You only need to add a time before the close Sleep (1) is OK
time.sleep(1)
ssh.close()