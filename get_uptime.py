import paramiko                     # for ssh
import os
import sys
import time


host = sys.argv[1]

def issue_command(transport, pause, command):
    chan = transport.open_session()
    chan.exec_command(command)

    buff_size = 1024
    stdout = b""
    stderr = b""

    while not chan.exit_status_ready():
        time.sleep(pause)
        if chan.recv_ready():
            stdout += chan.recv(buff_size)

        if chan.recv_stderr_ready():
            stderr += chan.recv_stderr(buff_size)

    exit_status = chan.recv_exit_status()
    while chan.recv_ready():
        stdout += chan.recv(buff_size)

    while chan.recv_stderr_ready():
        stderr += chan.recv_stderr(buff_size)

    return exit_status, stdout, stderr

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username='root', key_filename='/home/ryn/.ssh/id_rsa')
#ssh.connect(host, port=22, username=username, password=password, timeout=3,)
transport = ssh.get_transport()
pause = 1 

resp1 = issue_command(transport, pause, 'uptime')

print(resp1)
