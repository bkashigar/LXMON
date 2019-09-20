import sys
import os
from sys import exit
def trigger(cmd):
	print("================================================")
	os.system(cmd)
	print("================================================")
	return

print("================================================")
print("lxmon started ..................................")
print("================================================")
print(" 1 - Detils of Processes/CPU Usage/Memory/Disks etc...")
print(" 2 - List network statistics")
print(" 3 - Security information from linux processes")
option=int(input())
print(option)
if option==1:
	print("Processes/CPU Usage/Memory/Disks details")
	trigger('top')
elif option==2:
	print("List network statistics")
	trigger('netstat')
elif option==3:
	print("Security information from linux processes")
	trigger('ps -eM')
else:
	print("Enter proper option")
