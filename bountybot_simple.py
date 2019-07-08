import bountybot_library as bb
from spyse import spyse
import sys,json
website = sys.argv[1]
variable_timeout = 10
MysqlFTPTimeout = 5
for item in bb.getsubdomains(website):
	subdomain = item["domain"]
	print("Scanning " + subdomain)
	unclaimedsocialmedia = bb.getunclaimedsocialmedia(subdomain,variable_timeout)
	if bool(unclaimedsocialmedia) != False:
		print(("[{}] Unclaimed Social Media : " + json.dumps(unclaimedsocialmedia)).format(subdomain))
		pass

	if bb.tryftp(website,MysqlFTPTimeout) == True:
		print("[{}] Ftp (No Password)".format(subdomain))
		pass

	if bb.trymysql(website,3306,MysqlFTPTimeout)==True:
		print("[{}] Mysql (No Password) Port : 3306".format(subdomain))
		pass
	if bb.trymysql(website,9306,MysqlFTPTimeout)==True:
		print("[{}] Mysql (No Password) Port : 9306".format(subdomain))
		pass
	pass

	if bb.hostinjection(subdomain,variable_timeout) == True:
		print("[{}] Host Injection Detected!".format(subdomain))
		pass

	if bb.useragentsql(subdomain,variable_timeout) == True:
		print("[{}] User Agent Based SQL Injection Detected!".format(subdomain))
		pass

	if bb.cors(subdomain,variable_timeout) == True:
		print("[{}] Insecure Cors Found!".format(subdomain))
		pass
	pass