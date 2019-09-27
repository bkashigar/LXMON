import sys
import os
from sys import exit
def trigger(cmd):
	print("================================================")
	data=os.popen(cmd).read()
	print(data)
	print("================================================")
	return data

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
	data=trigger('top -l 1')
	heading="Processes/CPU Usage/Memory/Disks details"
elif option==2:
	print("List network statistics")
	data=trigger('netstat')
	heading="List network statistics"
elif option==3:
	print("Security information from linux processes")
	data=trigger('ps -eM')
	heading="Security information from linux processes"
else:
	print("Enter proper option")
	sys.exit()

hfile = open("Report.html","w")#write mode 
hfile.write("<!DOCTYPE html>\n") 
hfile.write("<html>\n")
hfile.write("<head>\n")
hfile.write("<title>Page Title</title>\n")
hfile.write("</head>\n")
hfile.write("<body>\n")
hfile.write("\n")
hfile.write("<h1>")
hfile.write(heading)
hfile.write("</h1>\n")
hfile.write("<p1>")
hfile.write(data)
hfile.write("</p1>\n")
hfile.write("</body>\n")
hfile.write("</html>\n")
hfile.close() 

