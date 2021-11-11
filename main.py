print('Xin Chào!')
print('Code Bởi Bin!')
print('Pass:chixiu')

referrer = input("[#] Nhập Pass :")
import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("title Code Viết Bởi Bin Hôi Ke")
os.system('cls' if os.name == 'nt' else 'clear')
print ("[+] Thông Tin:")
print ("[-] Mã Code Bình Thường ")
print ("[-] Phiên Bản: V1")
print ("--------")
print ("[+] Hãy NHớ Bin Hôi Ke VIẾT ") 
print ("[-] Hết!!") 
print ("[-] Youtube: bIN hÔI kE")
print ("--------")
referrer = input("[#] Nhập Pass Lại:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  Bình Thường" + " Bởi Bin Hôi KE")
		print("")
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] cHỜ cHút... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] Pass: {referrer}")    
		print(f"[:)] {g} Bin Hôi KE Code: Bình THường.")
		print(f"[#] Khuôn Mặt: {g} Tót {b} Xáu")
		print("[*] Hãy đợi 18 giây.")
		time.sleep(1)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  Bin Hôi KE VIẾT" + " Bình THường")
		print("")
		print("[:(] Lỗi :))))")
		print(f"[#] KhUÔN mẶT: {g} Tót {b} Xáu")	