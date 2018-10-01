import os
import requests
import datetime

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

today = datetime.datetime.now()
file_date = "_" + str(today.day) + "_" + str(today.month) + "_" + str(today.year)

def save_file(fund_name, file_link, file_type, payload, session, verify):
	if session == None:
		s = requests.Session()
	else:
		s = session
	if payload == None:
		if verify:
			file = s.get(url = file_link, headers = headers, stream = True)
		else:
			file = s.get(url = file_link, headers = headers, stream = True, verify = False)
	else:
		if verify:
			file = s.post(url = file_link, headers = headers, data = payload, stream = True)
		else:
			file = s.post(url = file_link, headers = headers, data = payload, stream = True, verify = False)
	
	foldername = file_date[1:]
	if foldername not in os.listdir():
		os.mkdir(foldername)
	file_name = foldername + "/" + fund_name + file_date + file_type
	with open(file_name, "wb") as f:
		f.write(file.content)
				
