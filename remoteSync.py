#!/usr/bin/python
import paramiko
client = SSHClient()
client.load_system_host_keys()
client.connect('192.168.0.39')
stdin, stdout, stderr = client.exec_command('ls -l')