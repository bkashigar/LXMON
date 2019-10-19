import sys
import getpass
import os
import paramiko
from sys import exit

def trigger(cmd,mname,user,pwd):
	print("Connecting to "+mname)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(mname, username=user, password=pwd)
	
	print("================================================")
	stdin, stdout, stderr = ssh.exec_command(cmd)
	#print(stdout.readlines())
	for line in iter(stdout.readline, ""):
    		print(line, end="")
	print("finished.....")
	print("================================================")
	
	ssh.close()
	return 'True'


print("================================================")
print("lxmon started ..................................")
print("================================================")

print("Please enter the machine name to monitor")
mname=str(input())
print("Please enter username")
user=str(input())
print("Please enter password")
pwd=getpass.getpass()

option=1
while option!=0:
	print(" 1 - Detils of Processes/CPU Usage/Memory/Disks etc...")
	print(" 2 - List network statistics")
	print(" 3 - Security information from linux processes")
	print(" 4 - Virtual Memory Statistics")
	print(" 5 - List Open Files")
	print(" 6 - Tcpdump – Network Packet Analyzer")
	print(" 7 - Iotop – Monitor Linux Disk I/O")
	print(" 0 - To exit")
	option=int(input())
	if option==1:
		print("Processes/CPU Usage/Memory/Disks details")
		data=trigger('top -l 1',mname,user,pwd)
	elif option==2:
		print("List network statistics")
		data=trigger('netstat',mname,user,pwd)
	elif option==3:
		print("Security information from linux processes")
		data=trigger('ps -eM',mname,user,pwd)
	elif option==4:
		print("Virtual Memory Statistics")
		data=trigger('vmstat',mname,user,pwd)
	elif option==5:
		print("List Open Files")
		data=trigger('lsof',mname,user,pwd)
	elif option==6:
		print("Tcpdump – Network Packet Analyzer")
		data=trigger('tcpdump -i eth0',mname,user,pwd)
	elif option==7:
		print("Iotop – Monitor Linux Disk I/O")
		data=trigger('iotop',mname,user,pwd)
	elif option==0:
		print("Exiting ... Bye!")
		sys.exit()
	else:
		print("Enter proper option")


