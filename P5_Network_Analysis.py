#python 3.5
#Project 5 - Network Analysis
#Author: Nolan Aubuchon
#Date: April 21, 2017
import re

choice = 0;
while(choice != 5):
	print("1.\tProtocol Analysis\r\n2.\tIP Address Analysis\r\n3.\tFTP Analysis\r\n4.\tMAC Address Analysis\r\n5.\tQUIT")
	choice = eval(input())
	if(choice == 1):
		"""
		PROTOCOL ANALYSIS
		-Finds list of Protocols and their percentage of total
		"""
		filename = input("Enter filename:\t")
		file = open(filename,"r")
		protocols = {}
		total = 0
		string = file.readline()
		while(string != ""):
			search = re.search(r'->\s+\S+\s+(\w+)',string)
			key = None
			if search != None:
				key = search.group(1)
			if key != None and key in protocols:
				protocols[key] = protocols[key] + 1
				total += 1
			elif key != None:
				protocols[key] = 1
				total += 1
			key = None
			string = file.readline()
		for line in protocols:
			print("%s:\t%d out of %d (%2.2f %%)" % (line,protocols[line],total,protocols[line]/total*100))
		file.close()
	elif(choice == 2):
		"""
		IP ADDRESS ANALYSIS
		-Finds all IP addresses that have connected to a specified IP address
		"""
		filename = input("Enter filename:\t")
		file = open(filename,"r")
		IP = input("Enter IP address:\t")
		IPs = []
		string = file.readline()
		while(string != ""):
			search = re.search(r'\s(\d+\.\d+\.\d+\.\d+)\s->\s(\d+\.\d+\.\d+\.\d+)\s',string)
			if search != None and IP == search.group(2) and search.group(1) not in IPs:
				IPs.append(search.group(1))
			string = file.readline()
		for ip in IPs:
			print(ip)
		file.close()
	elif(choice == 3):
		"""
		FTP ANALYSIS
		-Finds IP addresses of FTP servers
		-Finds FTP usernames and passwords
		"""
		filename = input("Enter filename:\t")
		file = open(filename,"r")
		users = {}
		user = []
		IPs = []
		flag = 0
		string = file.readline()
		while(string != ""):
			if flag == 0:
				search = re.search(r'FTP\s+\d+\s+Request:\s+USER\s+(\S+)',string)
				if search != None:
					user.append(search.group(1))
					flag = 1
			elif flag == 1:
				search = re.search(r'FTP\s+\d+\s+Request:\s+PASS\s+(\S+)',string)
				if search != None:
					user.append(search.group(1))
					flag = 2
			else:
				search = re.search(r'FTP\s+\d+\s+Response:\s+(\d+)',string)
				if search != None and search.group(1) == "230":
					users[user[0]] = user[1]
					user = []
					flag = 0
				elif search != None and search.group(1) == "530":
					user = []
					flag = 0
			search = re.search(r'->\s+(\S+)\sFTP',string)
			if search != None and search.group(1) not in IPs:
				IPs.append(search.group(1))
			string = file.readline()
		for use in users:
			print("username: %s, password: %s" % (use,users[use]))
		print("FTP IP ADDRESSES")
		for ip in IPs:
			print(ip)
		file.close()
	elif(choice == 4):
		"""
		MAC ADDRESS ANALYSIS
		-Finds MAC addresses and their associated IP addresses
		"""
		filename = input("Enter filename:\t")
		file = open(filename,"r")
		MACs = {}
		string = file.readline()
		while(string != ""):
			search = re.search(r'(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s*->\s*(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w).*Who has (\S*)\?.*Tell (\S*)',string)
			if search != None:
				MACs[search.group(1)] = search.group(4)
				MACs[search.group(2)] = search.group(3)
			string = file.readline()
		for key in MACs:
			print("%s <==> %s" % (key,MACs[key]))
		file.close()
	elif(choice != 5):
		print("Invalid Choice")
#END
