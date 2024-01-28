import paramiko
import os 

host = input("Enter IP address server:")
user = input("Enter username for login to server:")
secret = input("Enter password for login to server:")
port = int(input("Enter port for connection:"))

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
#stdin, stdout, stderr = client.exec_command('ls -la')
stdin, stdout, stderr = client.exec_command('show running-config')
data = stdout.read()
print("current config: ",data)
configFile = os.curdir + '/config.txt'
writer = open(configFile,'w')
writer.write(str(data))


