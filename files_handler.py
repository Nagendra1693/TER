import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import json
import downloader
import payload_data
# import json_parser_3

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

today = datetime.datetime.now()
file_date = "_" + str(today.day) + "_" + str(today.month) + "_" + str(today.year)

def get_aditya_birla():
	url = "https://mutualfund.adityabirlacapital.com/resources/total-expense-ratio"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = "https://mutualfund.adityabirlacapital.com/api/sitecore/ExpenseRatio/GetFundExpenseRatio"

	excel_template_raw = soup.find("input",{"id" : "ExcelTemplateId"})
	excel_template_soup = BeautifulSoup(str(excel_template_raw), "html.parser")
	excel_template = excel_template_soup.find("input",{"id" : "ExcelTemplateId"})["value"]

	yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
	months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

	start_date = "01-"+months[yesterday.month -1]+"-"+str(yesterday.year)
	end_date = str(yesterday.day)+"-"+months[yesterday.month -1]+"-"+str(yesterday.year)

	payload = {
		"ExcelTemplateId" : excel_template,
		"ClientIP": soup.find("input",{"id" : "ClientIP"})["value"],
		"ExcelTemplateRange" : soup.find("input",{"id" : "ExcelTemplateRange"})["value"],
		"ExcelFileName" : soup.find("input",{"id" : "ExcelFileName"})["value"],
		"ExpRatioFundName" : "allfunds",
		"ExpRatioFromDate" : start_date,
		"ExpRatioToDate": end_date
	}
	downloader.save_file(fund_name = "adityabirla", file_link = file_link, file_type = ".xlsx", payload = payload, session = None, verify = True)

def get_axis():
	url = "https://www.axismf.com/total-expense-ratio"	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	set_session_url = "https://www.axismf.com/TER/SetSession"
	session_data = soup.find("div", {"id" : "_Ter"}).find("div", {"class" : "col-sm-12"})

	session_payload = {
		"html" : str(session_data)
	}
	session = requests.Session()
	set_session = session.post(url = set_session_url, headers = headers, data = session_payload)

	today = datetime.datetime.now()
	day = str(today.day) if today.day > 9 else "0"+str(today.day)
	month = str(today.month) if today.month > 9 else "0"+str(today.month)

	start_date = str(today.year) + "-" + month + "-01"
	end_date = str(today.year) + "-" + month + "-" + day

	file_link = "https://www.axismf.com/TER/DownloadTer"
	payload = {
		"schemeCode": "ALL",
		"planMode": "ALL",
		"fromDate": start_date,
		"toDate": end_date
	}

	downloader.save_file(fund_name = "axis", file_link = file_link, file_type = ".html", payload = payload, session = session, verify = True)
def get_baroda():
	file_link = "https://online.barodapioneer.in/expenseratio/expenseratios.aspx"
	payload = payload_data.get_baroda_payload()
	downloader.save_file(fund_name = "baroda", file_link = file_link, file_type = ".xls", payload = payload, session = None, verify = True)
def get_bnpparibas():
	file_link = "https://www.bnpparibasmf.in/export/expense.xls"
	downloader.save_file(fund_name = "bnpparibas", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_boi():
	url = "https://www.boiaxamf.com/AjaxService.asmx/GetDocuments"
	payload = {
		"pagno":"0",
		"category":None,
		"fromDate":None,
		"toDate":None,
		"LibraryName":"InvestorCorner",
		"folderName":"TOTAL EXPENSE RATIO OF MF SCHEMES",
		"CategoryValue":"no"
	}

	page = requests.post(url = url, headers = headers, json= payload)
	json_response = json.loads(page.content)

	json_response_sub = json_response["d"]
	data_raw = json.loads(json_response_sub)
	file_link = data_raw["Documents"][0]["FolderUrl"]

	downloader.save_file(fund_name  = "boi", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_canara():
	url = "https://online.canararobeco.com/crmfexptest/expenseratio.aspx"
	downloader.save_file(fund_name = "canara", file_link = url, file_type = ".html", payload = None, session = None, verify = True)

def get_dhfl():
	url = "http://dhflpramericamf.com/statutory-disclosure/portfolio-related/expense-ratio"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")
 
	file_link = "http://dhflpramericamf.com"
	file_link += soup.find("div", {"id":"T486E3985025_Col00"}).find("div",{"class":"section-body"}).find("a",{"title":"Expense Ratio"})["href"]
	downloader.save_file(fund_name = "dhfl", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_edelweiss():
	url = "http://edelweissmf.com/StatutoryDisclosures/Expense.aspx"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	view_state = soup.find("input",{"id":"__VIEWSTATE"})["value"]
	view_state_generator = soup.find("input",{"id":"__VIEWSTATEGENERATOR"})["value"]

	file_link = "http://edelweissmf.com/StatutoryDisclosures/Expense.aspx"
	payload = {
		"__EVENTTARGET" : "ctl00$ContentPlaceHolder1$LbPath",
		"__EVENTARGUMENT" : "",
		"__VIEWSTATE" : view_state,
		"__VIEWSTATEGENERATOR" : view_state_generator,
		"__VIEWSTATEENCRYPTED" : ""
	}
	downloader.save_file(fund_name = "edelweiss", file_link = file_link, file_type = ".xls", payload = payload, session = None, verify = True)
def get_essel():
	url = "https://mutualfund.esselfinance.com/EsselMF_FileManager/dnd_others_expences_ratios.php"
	file_link = "https://mutualfund.esselfinance.com/EsselMF_FileManager/"
	
	page = requests.get(url = url, headers = headers, verify = False)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link += soup.find("div",{"class" : "inner_matter_right_area"}).find("a")["href"]
	downloader.save_file(fund_name = "essel", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = False)

def get_franklintempleton():
	url = "https://www.franklintempletonindia.com/content-international/data-files/en-in-retail/reportsdata.json"
	file_link = "https://www.franklintempletonindia.com/downloadsServlet/xls/"

	page = requests.get(url = url, headers = headers)
	json_response = json.loads(page.content)

	files_list = json_response["config"]["firstdropdown"][13]["dataRecords"]["linkdata"]
	for item in files_list:
		if item["assetType"] == "xlsx":
			name = item["name"]
			link = item["link"]
			break
	val = name.split(" ")
	for v in val:
		file_link += v.lower() + "-"
	file_link += link.split("docid=")[1]
	downloader.save_file(fund_name = "franklintempleton", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)

def get_hdfc():
	url = "https://cms.hdfcfund.com/en/hdfc/api/v1/ter/reports"
	payload = {
		"year" : "2018",
		"month" : "9"
	}
	page = requests.post(url = url, headers =headers, data = payload)

	json_response = json.loads(page.content)
	file_link = json_response["data"]["reports"]["files"][0]["file"]["url"]
	
	downloader.save_file(fund_name = "hdfc", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_hsbc():
	session = requests.Session()
	url = "https://www.camsonline.com/CAMS_Consent.aspx?ReturnUrl=%2fCOL_HSBCDownload.aspx"
	page = session.get(url = url, headers = headers)

	soup = BeautifulSoup(page.content, "html.parser")

	view_state = soup.find("input", {"id" : "__VIEWSTATE"})["value"]
	view_state_generator = soup.find("input", {"id" : "__VIEWSTATEGENERATOR"})["value"]
	payload = {
		"__VIEWSTATE" : view_state,
		"__VIEWSTATEGENERATOR": view_state_generator,
		"Proceed" : "rdo_accept",
		"btn_Proceed" : "PROCEED"
	}
	set_session = session.post(url = url, headers = headers, data = payload)

	file_link = "https://www.camsonline.com/COL_HSBCDownload.aspx"
	downloader.save_file(fund_name = "hsbc", file_link = file_link, file_type = ".xlsb", payload = None, session = session, verify = True)
def get_icici():
	url = "https://www.icicipruamc.com/Downloads/total-expense-ratio.aspx"

	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	event_target_raw = soup.find("div",{"class" : "DivContent"}).findAll("a")[1]["href"]
	
	start = event_target_raw.find("doPostBack('") + 12
	end = event_target_raw.find("','')", start)
	event_target = event_target_raw[start:end]

	payload = {
		"__EVENTTARGET" : event_target,
		"__EVENTARGUMENT" : "",
		"__VIEWSTATE" : soup.find("input",{"id" : "__VIEWSTATE"})["value"],
		"__VIEWSTATEGENERATOR" : soup.find("input",{"id" : "__VIEWSTATEGENERATOR"})["value"],
		"ctl00$SiteSearch$SearchBox1$ctl00$ctl00$queryText" : "Site Search",
		"ddlGroupLinks" : "--- ICICI Bank Group Links ---"
		}
	downloader.save_file(fund_name = "icici", file_link = url, file_type = ".xlsx", payload = payload, session = None, verify = True)
def get_idbi():
	url = "https://www.idbimutual.co.in/statutory-disclosure/total-expense-ratio-of-mutual-fund-schemes"

	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link ="https://www.idbimutual.co.in" + soup.find("table", {"class","our_invester_type_table footable"}).find("a")["href"]

	downloader.save_file(fund_name = "idbi", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_idfc():
	url = "https://www.idfcmf.com/total-expense-ratio.aspx"

	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = "https://www.idfcmf.com/" + soup.find("div",{"class" : "quick_access_tab_cont expenses-ratioMF"}).find("a")["href"][2:]

	downloader.save_file(fund_name = "idfc", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_iifcl():
	url = "http://iifclmf.com/investor-relations/grievance-redressal/"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = ""
	links = soup.find_all("a")
	for link in links:
		if link["href"].find("TER-Data") != -1:
			file_link = link["href"]
			break
	downloader.save_file(fund_name = "iifcl", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_iifl():
	file_link = "https://www.iiflmf.com/expense-ratio-data/download"
	downloader.save_file(fund_name = "iifl", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_ilfs():
	file_link = "http://www.ilfsinfrafund.com/otherfile/TER_IL&FS_MF_IDF.xls"
	downloader.save_file(fund_name = "ilfs", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_indiabulls():
	url = "http://www.indiabullsamc.com/downloads/total-expense-ratio-of-mutual-fund-schemes/"
	page = requests.get(url = url, headers= headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = ""
	links = soup.find("div", {"class":"financial-name"}).findAll("a")
	for link in links:
		if link.get_text().find("Total Expense Ratio for all Schemes") != -1:
			file_link = link["href"]
			break
	downloader.save_file(fund_name = "indiabulls", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_invesco():
	url = "https://invescomutualfund.com/api/TotalExpenseRatioOfMutualFundSchmes?year="+str(today.year)
	page = requests.get(url = url,headers = headers)
	json_response = json.loads(page.content)
	file_link = json_response[0]["tabYear"][0]["finan"][0]["Url"]

	downloader.save_file(fund_name = "invesco", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_jmfinancial():
	file_link = "http://www.jmfinancialmf.com/CMT/Upload/TER/TER%20Format.xlsx"
	downloader.save_file(fund_name = "jmfinancial", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_kotak():
	session = requests.Session()
	url = "https://assetmanagement.kotak.com/total-expense-ratio"
	
	page = session.get(url = url, headers= headers)
	soup = BeautifulSoup(page.content, "html.parser")

	form = soup.find("table", {"class":"product-table"}).findAll("form")[-1]
	file_link = form["action"]

	payload = {
		form.find("input")["name"] : form.find("input")["value"]
	}
	downloader.save_file(fund_name = "kotak", file_link = file_link, file_type = ".xls", payload = payload, session = session, verify = True)
def get_ltfs():
	url = "https://www.ltfs.com/companies/lnt-investment-management/downloads.html"

	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = "https://www.ltfs.com" + soup.find("div", {"class":"dynamic-asset-values-noticesdownloads_1699538133"}).findAll("div",{"class":"mr-notice-content-wrap"})[0].find("a")["href"]

	downloader.save_file(fund_name = "ltfs", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_lic():
	session = requests.Session()
	url = "https://www.licmf.com/Total_Expense_Ratio"
	
	set_session = session.get(url = url, headers= headers, verify= False)

	file_link = "https://www.licmf.com/Total_Expense_Ratio/get_hist_exp_rat"

	day = str(today.day) if today.day > 9 else "0"+str(today.day)
	month = str(today.month) if today.month > 9 else "0"+str(today.month)

	start_date = "01-" + month + "-" + str(today.year)
	end_date = day + "-" + month + "-" + str(today.year)

	payload = {
		"cat" : "all",
		"scheme" : "all",
		"plan" : "ALL",
		"rang": "D",
		"from_date" : start_date,
		"todate" : end_date
	}
	downloader.save_file(fund_name = "lic", file_link = file_link, file_type = ".html", payload = payload, session = None, verify = False)
def get_mahindra():
	url = "https://www.mahindramutualfund.com/downloads#ter"

	page = requests.get(url = url, headers= headers)
	soup = BeautifulSoup(page.content,"html.parser")

	containers = soup.findAll("div",{"class":"acc_container"})
	file_link = "https://www.mahindramutualfund.com/"
	for c in containers:
		title = c.find("a").get_text()
		if title == "Total Expense Ratio":
			file_link += c.find("ul",{"class" : "download-pdf"}).findAll("a")[-1]["href"]
			break

	downloader.save_file(fund_name = "mahindra", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_mirae():
	url = "https://www.miraeassetmf.co.in/downloads/total-expense-ratio"
	page = requests.get(url = url, headers= headers)
	soup = BeautifulSoup(page.content,"html.parser")

	file_link = soup.find("table",{"class":"table table-archive"}).find("tbody").findAll("tr")[0].findAll("td")[1].find("a")["href"]

	downloader.save_file(fund_name = "mirae", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_motilal():
	session = requests.Session()
	url = "https://www.motilaloswalmf.com/downloads/mutual-fund/totalexpenseratio"
	
	page = session.get(url = url, headers= headers)
	soup = BeautifulSoup(page.content,"html.parser")

	view_state = soup.find("input",{"id" : "__VIEWSTATE"})["value"]
	event_validation = soup.find("input",{"id" : "__EVENTVALIDATION"})["value"]
	payload = {
		"ctl00_ToolkitScriptManager1_HiddenField": "",
		"__EVENTTARGET": "",
		"__EVENTARGUMENT": "",
		"__VIEWSTATE": view_state,
		"__VIEWSTATEENCRYPTED": "",
		"__EVENTVALIDATION": event_validation,
		"ctl00$ContentPlaceHolder1$schemdrp": "",
		"ctl00$ContentPlaceHolder1$btnExcel.x": "28",
		"ctl00$ContentPlaceHolder1$btnExcel.y": "21",
		"ctl00$Ucfooter1$nwsletter": "Email Address"
	}
	downloader.save_file(fund_name = "motilal", file_link = url, file_type = ".xls", payload = payload, session = session, verify = True)
def get_ppfas():
	url = "https://amc.ppfas.com/statutory-disclosures/total-expense-ratio-TER/"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link =soup.find("div",{"class" : "section-white"}).find("div", {"class" : "col-sm-12"}).findAll("a")[1]["href"]
	
	downloader.save_file(fund_name = "ppfas", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_principal():
	url = "https://www.principalindia.com/downloads-disclosures.aspx"

	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = "https://www.principalindia.com" + soup.find("div",{"id" : "collapse-6"}).findAll("a")[-1]["href"][2:]

	downloader.save_file(fund_name = "principal", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_quant():
	url = "http://www.escortsmutual.com/statutory-disclosures.aspx"

	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	links = soup.findAll("table")[3].findAll("a")
	
	for link in links:
		if link.get_text().find("Total Expense Ratio of Scheme") != -1:
			file_link = link["href"]
			break
	downloader.save_file(fund_name = "quant", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_quantum():
	session = requests.Session()

	url = "https://www.quantumamc.com/Totalexpenseratio.aspx"
	set_session = session.get(url = url, headers = headers)

	file_link = "https://www.quantumamc.com/AjaxMain/Common.aspx?FuncName=SEBIExportExcel"
	downloader.save_file(fund_name = "quantum", file_link = file_link, file_type = ".xlsx", payload = None, session = session, verify = True)
def get_reliance():
	url = "https://www.reliancemutual.com/Pages/Total-Expense-Ratio-of-Mutual-Fund-Schemes.aspx"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = "https://www.reliancemutual.com" + soup.findAll("ul",{"class" : "pdf"})[0].findAll("a")[0]["href"]
	downloader.save_file(fund_name = "reliance", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_sahara():
	url = "http://www.saharamutual.com/downloads/TotalExpenseRatio.aspx"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = "http://www.saharamutual.com" + soup.find("div",{"id" : "m1"}).findAll("a")[0]["href"][2:]
	downloader.save_file(fund_name = "sahara", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_sbi():
	file_link = "https://www.sbimf.com/en-us/TER_Allschemes/Ter_AllSchemes.xlsx"
	downloader.save_file(fund_name = "sbi", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)
def get_shriram():
	session = requests.Session()

	url = "http://shriramamc.com/TER-Latest.aspx"
	headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

	page = session.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")


	view_state = soup.find("input", {"id" : "__VIEWSTATE"})["value"]
	event_validation = soup.find("input", {"id" : "__EVENTVALIDATION"})["value"]
	view_state_generator = soup.find("input", {"id" : "__VIEWSTATEGENERATOR"})["value"]

	payload = {
		"__EVENTTARGET": "ctl00$ContentPlaceHolder1$dpFund",
		"__EVENTARGUMENT": "",
		"__LASTFOCUS": "",
		"__VIEWSTATE": view_state,
		"__VIEWSTATEGENERATOR": view_state_generator,
		"__EVENTVALIDATION": event_validation,
		"ctl00$ContentPlaceHolder1$dpFund": "1",
		"ctl00$ContentPlaceHolder1$dpScheme": "0"
	}

	page = session.post(url = url, headers = headers, data = payload)
	soup = BeautifulSoup(page.content, "html.parser")

	view_state = soup.find("input", {"id" : "__VIEWSTATE"})["value"]
	event_validation = soup.find("input", {"id" : "__EVENTVALIDATION"})["value"]
	view_state_generator = soup.find("input", {"id" : "__VIEWSTATEGENERATOR"})["value"]

	payload = {
		"__EVENTTARGET" : "",
		"__EVENTARGUMENT" : "",
		"__LASTFOCUS" : "",
		"__VIEWSTATE" : view_state,
		"__VIEWSTATEGENERATOR" : view_state_generator,
		"__EVENTVALIDATION" : event_validation,
		"ctl00$ContentPlaceHolder1$dpFund" : "1",
		"ctl00$ContentPlaceHolder1$dpScheme" : "1",
		"ctl00$ContentPlaceHolder1$SubmitImg.x" : "35",
		"ctl00$ContentPlaceHolder1$SubmitImg.y" : "17"
	}
	downloader.save_file(fund_name = "shriram", file_link = url, file_type = ".html", payload = payload, session = session, verify = True)
def get_sundaram():
	session = requests.Session()
	url = "https://www.sundarammutual.com/TER"
	page = session.get(url= url, headers = headers)

	file_link = "https://www.sundarammutual.com"
	soup = BeautifulSoup(page.content, "html.parser")
	scripts = soup.findAll("script")
	for script in scripts:
		try:
			if script["src"].find("/ajaxpro/Views_TER,App_Web") != -1:
				file_link += script["src"]
				break
		except:
			pass

	headers2 = {
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
		"X-AjaxPro-Method": "DailyTER"
	}

	page = session.post(url = file_link, headers = headers2, json = {})

	json_response = json.loads(page.content)

	foldername = file_date[1:]
	if foldername not in os.listdir():
		os.mkdir(foldername)

	file_name = foldername + "/" + "sundaram" + file_date + ".json"
	with open(file_name,"w") as f:
		json.dump(json_response,f)
def get_tata():
	url = "http://www.tatamutualfund.com/our-funds/total-expense-ratio"
	
	page = requests.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	file_link = "http://www.tatamutualfund.com" + soup.findAll("ul",{"class" : "XlsList"})[0].find("a")["href"]
	downloader.save_file(fund_name = "tata", file_link = file_link, file_type = ".xls", payload = None, session = None, verify = True)
def get_taurus():
	url = "https://www.taurusmutualfund.com/getfundlist.php"
	payload = {
		"action" : "getinfo"
	} 

	page = requests.post(url = url, headers = headers, data = payload)
	json_response = json.loads(page.content)
	json_response = json_response["tablelog"]

	foldername = file_date[1:]
	if foldername not in os.listdir():
		os.mkdir(foldername)

	file_name = foldername + "/" + "taurus" + file_date + ".html"
	with open(file_name,"w") as f:
		json.dump(json_response,f)
def get_union():
	session = requests.Session()
	url = "http://unionmf.com/downloads/TotalExpenseRatioOfMutualFundSchemes.aspx"
	
	page = session.get(url = url, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")

	links = soup.findAll("a")

	file_link = ""
	for link in links:
		if link.get_text().find("Total Expense Ratio of Mutual Fund Schemes") != -1:
			file_link = link["href"]

	downloader.save_file(fund_name = "union", file_link = file_link, file_type = ".xlsx", payload = None, session = session, verify = True)
def get_uti():
	day = str(today.day) if today.day > 9 else "0"+str(today.day)
	month = str(today.month) if today.month > 9 else "0"+str(today.month)

	start_date = str(today.year) + "-" + month + "-01"
	end_date = str(today.year) + "-" + month + "-" + day

	file_link = "https://www.utimf.com/get-scheme-ter/?from_date=2018-09-01&to_date=2018-09-20".format(start_date,end_date)

	downloader.save_file(fund_name = "uti", file_link = file_link, file_type = ".xlsx", payload = None, session = None, verify = True)

issues = list()

try:
	get_aditya_birla()
except:
	issues.append("aditya")
try:
	get_axis()
except:
	issues.append("axis")
try:
	get_baroda()
except:
	issues.append("baroda")
try:
	get_bnpparibas()
except:
	issues.append("bnp")
try:
	get_boi()
except:
	issues.append("boi")
try:
	get_canara()
except:
	issues.append("canara")
try:
	get_dhfl()
except:
	issues.append("dhfl")
try:
	get_edelweiss()
except:
	issues.append("edelweiss")
try:
	get_essel()
except:
	issues.append("essel")
try:
	get_franklintempleton()
except:
	issues.append("franklintempleton")
try:
	get_hdfc()
except:
	issues.append("hdfc")
try:
	get_hsbc()
except:
	issues.append("hsbc")
try:
	get_icici()
except:
	issues.append("icici")
try:
	get_idbi()
except:
	issues.append("idbi")
try:
	get_idfc()
except:
	issues.append("idfc")
try:
	get_iifcl()
except:
	issues.append("iifcl")
try:
	get_iifl()
except:
	issues.append("iifl")
try:
	get_ilfs()
except:
	issues.append("ilfs")
try:
	get_indiabulls()
except:
	issues.append("indiabulls")
try:
	get_invesco()
except:
	issues.append("invesco")
try:
	get_jmfinancial()
except:
	issues.append("jmfinancial")
try:
	get_kotak()
except:
	issues.append("kotak")
try:
	get_ltfs()
except:
	issues.append("ltfs")
try:
	get_lic()
except:
	issues.append("lic")
try:
	get_mahindra()
except:
	issues.append("mahindra")
try:
	get_mirae()
except:
	issues.append("mirae")
try:
	get_motilal()
except:
	issues.append("motilal")
try:
	get_ppfas()
except:
	issues.append("ppfas")
try:
	get_principal()
except:
	issues.append("principal")
try:
	get_quant()
except:
	issues.append("quant")
try:
	get_quantum()
except:
	issues.append("quantum")
try:
	get_reliance()
except:
	issues.append("reliance")
try:
	get_sahara()
except:
	issues.append("sahara")
try:
	get_sbi()
except:
	issues.append("sbi")
try:
	get_shriram()
except:
	issues.append("shriram")
try:
	get_sundaram()
except:
	issues.append("sundaram")
try:
	get_tata()  
except:
	issues.append("tata")
try:
	get_taurus()
except:
	issues.append("taurus")
try:
	get_union()
except:
	issues.append("union")
try:
	get_uti()
except:
	issues.append("uti")

if len(issues) > 0:
	print(issues)