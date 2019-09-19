import os

def trigger(cmd):
	os.system(cmd)
	return

print("================================================")
print("lxmon started ..................................")
print("================================================")
print("1 - List of files in directory\n2- Detils of Processes/CPU Usage/Memory/Disks etc...")
option=int(input())
print(option)
if option==1:
	print("================================================")
	print("List of files in directory")
	print("================================================")
	trigger('ls -ltraR')
	print("================================================")
	print("Current working directory")
	trigger('pwd')
	print("================================================")
elif option==2:
	print("================================================")
	print("Processes/CPU Usage/Memory/Disks details")
	trigger('top')
	print("================================================")
