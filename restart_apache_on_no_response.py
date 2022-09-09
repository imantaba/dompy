import requests                     # for check port 80/443
from requests import exceptions
import paramiko                     # for ssh
import os
import sys
import time

# YOU MUST SET Environment variable REMOTE_APACHE_USER and REMOTE_APACHE_PASS


host = sys.argv[1]
url = "http://{0}/".format(host)
response = None
retry_attempts = 3

#command to execute on the remote server
command = "sudo service apache2 restart"

while response is None and retry_attempts > 0:
    try:
        response = requests.get(url=url)
    except exceptions.ConnectionError as e:
        if "REMOTE_APACHE_PASS" not in os.environ or 'REMOTE_APACHE_USER' not in os.environ:
            print("user/password not found, exiting")
            exit()

        # Create SSH client and set Auto Add policy to add host to ~/.ssh/known_hosts file
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        #Connect to host
        ssh.connect(hostname=host, username=os.environ['REMOTE_APACHE_USER'], password=os.environ["REMOTE_APACHE_PASS"])
        
        # Invoke a separate shell to execute command
        shell = ssh.invoke_shell()
        shell.send(command + "\n")
        
        # Wait if necessary
        time.sleep(5)
        
        # Get the console messages on the screen and print them. This can be used for verifying output as well using regex
        rec_buffer = shell.recv(1024)
        print(rec_buffer)
        retry_attempts -= 1

if response.status_code == 200:
    print("Successfully displayed the name")

assert response.status_code == 200, "Response code expected - 200, got {0}\n\nResponse content\n\n{1}".format(response.status_code, response.content)
