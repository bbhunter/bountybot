### Importing Libs Start
import requests,pyfiglet,pymysql,socket,re,json,ipaddress
from spyse import spyse
from ftplib import FTP
### Importing Libs End

totalreq = 0

def printbanner():
	print(pyfiglet.figlet_format("BountyBot"))
	print("twitter.com/rootxyele")
	print("github.com/xyele")
	pass

def trymysql(ihost,iport,itimeout):
	try:
		mysqlcon = pymysql.connect(host=ihost,port=iport,user="root",passwd="", connect_timeout=itimeout)
		mysqlcur = mysqlcon.cursor()
		mysqlcur.execute('SET NAMES UTF8')
		return True
		pass
	except Exception as e:
		return False
		pass
	pass

def cors(iwebsite,itimeout):
	corsHeaders = {"Origin":"https://evil.com","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.170"}
	try:
		r = requests.get("http://" + iwebsite, allow_redirects=True, timeout=itimeout)
		if "Access-Control-Allow-Credentials" in r.headers and "Access-Control-Allow-Origin" in r.headers and "Access-Control-Allow-Methods" in r.headers:
			if (r.headers["Access-Control-Allow-Credentials"] == "true") and (r.headers["Access-Control-Allow-Origin"] == "https://evil.com"):
				return True
				pass
			else:
				return False
				pass
			pass
		else:
			return False
			pass
		pass
	except Exception as e:
		return False
		pass
	pass

def tryftp(ihost,itimeout):
	try:
		ftp = FTP(ihost,itimeout=10)
		if "Login successful" in ftp.login():
			ftp.quit()
			return True
			pass
		else:
			return False
			pass
		pass
	except Exception as e:
		return False
		pass

def hostinjection(iwebsite,itimeout):
	try:
		rheaders = {"Host":"helloiamsuperhuman.com"}
		r = requests.get("http://"+iwebsite,headers=rheaders,allow_redirects= False, timeout=itimeout)
		if "helloiamsuperhuman.com" in r.headers["Location"]:
			return True
			pass
		else:
			return False
			pass
		pass
	except Exception as e:
		return False
		pass
	pass

def getsubdomains(iwebsite):
	try:
		s = spyse()
		subdomains = s.subdomains(iwebsite, param="domain")["records"]
		return subdomains
		pass
	except Exception as e:
		subdomains = []
		subdomains.append({"domain":iwebsite})
		return subdomains
		pass
	pass

def getunclaimedsocialmedia(iwebsite,itimeout):
	try:
		r = requests.get("http://" + iwebsite, allow_redirects=True, timeout=itimeout).text
		unclaimed = []
		status = 0
		facebook = re.findall("href=\"https://www.facebook.com/(.*?)\"",r)
		twitter = re.findall("href=\"https://www.twitter.com/(.*?)\"",r)
		instagram = re.findall("href=\"https://www.instagram.com/(.*?)/\"",r)
		for username in facebook:
			username = username.split("/")[0]
			if checkclaimed("facebook",username) == False:
				unclaimed.append(["facebook",username])
				status = 1
				pass
			pass
		for username in twitter:
			username = username.split("/")[0]
			if checkclaimed("twitter",username) == False:
				unclaimed.append(["Twitter",username])
				status = 1
				pass
			pass
		for username in instagram:
			username = username.split("/")[0]
			if checkclaimed("instagram",username) == False:
				unclaimed.append(["Instagram",username])
				status = 1
				pass
			pass
		return unclaimed
		pass
	except Exception as e:
		return False
		pass
	pass

def checkclaimed(iplatform,iusername):
	try:
		r = requests.get("https://username-availability.herokuapp.com/check/{}/{}".format(iplatform,iusername)).text
		claim = json.loads(r)["status"]
		if claim == 200:
			return True
			pass
		elif claim == 500:
			return True
			pass
		else:
			return False
			pass
		pass
	except Exception as e:
		return False
		pass

def useragentsql(ihost,itimeout):
	sqlpayload = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep({}*2),0))OR'".format(str(itimeout))
	sqlheaders = {"User-Agent":sqlpayload}
	try:
		r = requests.get("http://" + ihost,headers = sqlheaders,allow_redirects=True, timeout=itimeout)
		return False
		pass
	except Exception as e:
		try:
			r = requests.get("http://" + ihost,allow_redirects=True, timeout=itimeout)
			return True
			pass
		except Exception as e:
			return False
			pass
		pass
	pass
