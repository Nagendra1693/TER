from bs4 import BeautifulSoup
import pandas as pd
import json
import xlrd

from pyxlsb import open_workbook as open_xlsb
from datetime import datetime

today = datetime.now()
file_date = "_" + str(today.day) + "_" + str(today.month) + "_" + str(today.year)

foldername = file_date[1:]

def get_data_shriram():
	file_name = foldername + "/" + "shriram" + file_date + ".html"
	data = list()
	soup = BeautifulSoup(open(file_name),"html.parser")
	row = soup.find("div",{"id" : "ctl00_ContentPlaceHolder1_data"}).findAll("tr")[-1]
	col = row.findAll("td")
	
	date = col[0].get_text().split("/")
	day = date[0]
	month = date[1]
	year = date[2]
	date_final = month + "-" + day + "-" + year

	entry = {
		"Name of scheme" : "Shriram Hybrid Equity Fund",
		"Date" : date_final,
		"REGULAR_Base_TER_perc" : col[1].get_text(),
		"REGULAR_Addnl_52_6a_b_exp_perc" : col[2].get_text(),
		"REGULAR_Addnl_52_6a_c_exp_perc" : col[3].get_text(),
		"REGULAR_GST_perc" : col[4].get_text(),
		"REGULAR_Total_ter_perc" : col[5].get_text(),
		"DIRECT_Base_TER_perc" : col[6].get_text(),
		"DIRECT_Addnl_52_6a_b_exp_perc" : col[7].get_text(),
		"DIRECT_Addnl_52_6a_c_exp_perc" : col[8].get_text(),
		"DIRECT_GST_perc" : col[9].get_text(),
		"DIRECT_Total_ter_perc" : col[10].get_text()
	}
	data.append(entry)
	return data

def get_data_sundaram():
	file_name = foldername + "/" + "sundaram" + file_date + ".json"
	# file_name = "testing.json"
	def remove_per(inp):
		i = inp.find("%")
		if i != -1:
			return inp[:(i-1)]
		else:
			return inp
	data = list()
	with open(file_name,"r") as f:
		json_response_raw = json.load(f)
	json_response_value = json_response_raw["value"]
	json_response = json.loads(json_response_value)
	for row in json_response:
		entry = {
			"Name of scheme" : row["Group_Name"],
			"Date" : row["Ter_Date_Disp"],
			"REGULAR_Base_TER_perc" : remove_per(row["Reg_Ba_Ter_Disp"]),
			"REGULAR_Addnl_52_6a_b_exp_perc" : remove_per(row["Reg_Addl_Exp_526Ab_Disp"]),
			"REGULAR_Addnl_52_6a_c_exp_perc" : remove_per(row["Reg_Addl_Exp_526Ac_Disp"]),
			"REGULAR_GST_perc" : remove_per(row["Reg_Gst_Disp"]),
			"REGULAR_Total_ter_perc" : remove_per(row["Reg_Tot_Ter_Disp"]),
			"DIRECT_Base_TER_perc" : remove_per(row["Dp_Ba_Ter_Disp"]),
			"DIRECT_Addnl_52_6a_b_exp_perc" : remove_per(row["Dp_Addl_Exp_526Ab_Disp"]),
			"DIRECT_Addnl_52_6a_c_exp_perc" : remove_per(row["Dp_Addl_Exp_526Ac_Disp"]),
			"DIRECT_GST_perc" : remove_per(row["Dp_Gst_Disp"]),
			"DIRECT_Total_ter_perc" : remove_per(row["Dp_Tot_Ter_Disp"])
		}
		data.append(entry)
	return data
def get_data_boi():
	file_name = foldername + "/" + "boi" + file_date + ".xlsx"
	wb = xlrd.open_workbook(file_name) 
	sheet = wb.sheet_by_index(0)
	rows = sheet.nrows
	data = list()
	scheme_name = ""
	for i in range(2,rows):
		cells = sheet.row_slice(rowx = i, start_colx = 0, end_colx = 12)
		if scheme_name == "":
			scheme_name = cells[0].value
		elif scheme_name != "" and cells[0].value != "":
			scheme_name = cells[0].value
		if cells[2].value != "":
			date = xlrd.xldate.xldate_as_datetime(cells[1].value, wb.datemode).strftime('%m-%d-%Y')
			def clean(inp):
				inp = inp * 100
				inp = "{0:.2f}".format(inp)
				return inp
			entry = {
				"Name of scheme" : scheme_name,
				"Date" : date,
				"REGULAR_Base_TER_perc" : clean(cells[2].value),
				"REGULAR_Addnl_52_6a_b_exp_perc" : clean(cells[3].value),
				"REGULAR_Addnl_52_6a_c_exp_perc" : clean(cells[4].value),
				"REGULAR_GST_perc" : clean(cells[5].value),
				"REGULAR_Total_ter_perc" : clean(cells[6].value),
				"DIRECT_Base_TER_perc" : clean(cells[7].value),
				"DIRECT_Addnl_52_6a_b_exp_perc" : clean(cells[8].value),
				"DIRECT_Addnl_52_6a_c_exp_perc" : clean(cells[9].value),
				"DIRECT_GST_perc" : clean(cells[10].value),
				"DIRECT_Total_ter_perc" : clean(cells[11].value)
			}
						
			data.append(entry)

	return data

def get_data_sahara():
	file_name = foldername + "/" + "sahara" + file_date + ".xls"
	wb = xlrd.open_workbook(file_name) 
	sheet = wb.sheet_by_index(0)
	rows = sheet.nrows
	data = list()
	funds = list()
	for i in range(4,rows):
		cells = sheet.row_slice(rowx = i, start_colx = 0, end_colx = 1)
		if cells[0].value == "":
			break
		funds.append(cells[0].value)
	for i in range(4,rows):
		cells = sheet.row_slice(rowx = i, start_colx = 2, end_colx = 14)
		if cells[2].value != "":
			date = xlrd.xldate.xldate_as_datetime(cells[0].value, wb.datemode).strftime('%m-%d-%Y')
			for fund in funds:
				entry = {
					"Name of scheme" : fund,
					"Date" : date,
					"REGULAR_Base_TER_perc" : cells[1].value,
					"REGULAR_Addnl_52_6a_b_exp_perc" : cells[2].value,
					"REGULAR_Addnl_52_6a_c_exp_perc" : cells[3].value,
					"REGULAR_GST_perc" : cells[4].value,
					"REGULAR_Total_ter_perc" : cells[5].value,
					"DIRECT_Base_TER_perc" : cells[7].value,
					"DIRECT_Addnl_52_6a_b_exp_perc" : cells[8].value,
					"DIRECT_Addnl_52_6a_c_exp_perc" : cells[9].value,
					"DIRECT_GST_perc" : cells[10].value,
					"DIRECT_Total_ter_perc" : cells[11].value
				}
								
				data.append(entry)
	sheet2 = wb.sheet_by_index(1)
	rows2 = sheet2.nrows
	scheme = sheet2.row_slice(rowx = 2, start_colx = 0, end_colx = 2)[1].value
	for i in range(5,rows2):
		cells = sheet2.row_slice(rowx = i, start_colx = 0, end_colx = 14)
		if cells[2].value != "":
			date = xlrd.xldate.xldate_as_datetime(cells[0].value, wb.datemode).strftime('%m-%d-%Y')
			entry = {
				"Name of scheme" : scheme,
				"Date" : date,
				"REGULAR_Base_TER_perc" : cells[1].value,
				"REGULAR_Addnl_52_6a_b_exp_perc" : cells[2].value,
				"REGULAR_Addnl_52_6a_c_exp_perc" : cells[3].value,
				"REGULAR_GST_perc" : cells[4].value,
				"REGULAR_Total_ter_perc" : cells[5].value,
				"DIRECT_Base_TER_perc" : cells[7].value,
				"DIRECT_Addnl_52_6a_b_exp_perc" : cells[8].value,
				"DIRECT_Addnl_52_6a_c_exp_perc" : cells[9].value,
				"DIRECT_GST_perc" : cells[10].value,
				"DIRECT_Total_ter_perc" : cells[11].value
			}
								
			data.append(entry)
				
	return data
def get_data_ppfas():
	file_name = foldername + "/" + "ppfas" + file_date + ".xlsx"
	wb = xlrd.open_workbook(file_name) 
	sheet = wb.sheet_by_index(0)
	rows = sheet.nrows
	data = list()
	funds = list()
	indexs = list()
	for i in range(0,rows):
		scheme = sheet.row_slice(rowx = i, start_colx = 0, end_colx = 1)[0].value
		try:
			if scheme.find("Name of Scheme: ") != -1:
				funds.append(scheme)
				indexs.append(i)
		except:
			pass
	indexs.append(rows)
	for j in range(2):
		for i in range(indexs[j]+3,indexs[j+1]-1):
			cells = sheet.row_slice(rowx = i, start_colx = 0, end_colx = 12)
			if cells[2].value != "":
				date = cells[0].value
				if type(date) == str:
					actual_date = date.split("/")
					day = actual_date[0]
					month = actual_date[1]
					year = actual_date[2]
					date = month + "-" + day + "-" + year
				else:
					date = xlrd.xldate.xldate_as_datetime(date, wb.datemode).strftime('%m-%d-%Y') 
				entry = {
					"Name of scheme" : funds[j][len("Name of Scheme: "):],
					"Date" : date,
					"REGULAR_Base_TER_perc" : cells[1].value,
					"REGULAR_Addnl_52_6a_b_exp_perc" : cells[2].value,
					"REGULAR_Addnl_52_6a_c_exp_perc" : cells[3].value,
					"REGULAR_GST_perc" : cells[4].value,
					"REGULAR_Total_ter_perc" : cells[5].value,
					"DIRECT_Base_TER_perc" : cells[6].value,
					"DIRECT_Addnl_52_6a_b_exp_perc" : cells[7].value,
					"DIRECT_Addnl_52_6a_c_exp_perc" : cells[8].value,
					"DIRECT_GST_perc" : cells[9].value,
					"DIRECT_Total_ter_perc" : cells[10].value
				}				
				data.append(entry)
	return data

# This method convert value from percentage to actual value 
def render_value(inp):
	inp *= 100
	inp ="{0:.2f}".format(inp)
	return inp
# This converts excel date to normal date
def render_date(date):
	dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(date) - 2)
	return dt.strftime('%m-%d-%Y')

def get_data_hsbc():
	file_name = foldername + "/" + "hsbc" + file_date + ".xlsb"
	wb = open_xlsb(file_name)
	data = list()
	sheets = len(wb.sheets)
	for i in range(2,sheets):
		sheet = wb.get_sheet(i)
		i = 0
		for row in sheet.rows():
			cells = list(row)
			if i == 2:
				scheme_name = cells[2][2]
			if i >= 6:
				if cells[2][2] != None:
					entry = {
						"Name of scheme" : scheme_name,
						"Date" : render_date(cells[1][2]),
						"REGULAR_Base_TER_perc" : render_value(cells[2][2]),
						"REGULAR_Addnl_52_6a_b_exp_perc" : render_value(cells[3][2]),
						"REGULAR_Addnl_52_6a_c_exp_perc" : render_value(cells[4][2]),
						"REGULAR_GST_perc" : render_value(cells[5][2]),
						"REGULAR_Total_ter_perc" : render_value(cells[6][2]),
						"DIRECT_Base_TER_perc" : render_value(cells[9][2]),
						"DIRECT_Addnl_52_6a_b_exp_perc" : render_value(cells[10][2]),
						"DIRECT_Addnl_52_6a_c_exp_perc" : render_value(cells[11][2]),
						"DIRECT_GST_perc" : render_value(cells[12][2]),
						"DIRECT_Total_ter_perc" : render_value(cells[13][2])
					}
									
					data.append(entry)
			i+=1
	return data