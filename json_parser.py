from bs4 import BeautifulSoup
import json
import pandas as pd
import datetime
import xlrd
import data_values
today = datetime.datetime.now()
file_date = "_" + str(today.day) + "_" + str(today.month) + "_" + str(today.year)

foldername = file_date[1:]

def render_value(inp,data_filter):
	if data_filter != None and inp != "":
		inp *= 100
		inp ="{0:.2f}".format(inp)
	return inp

def get_data(fund_name, file_type,index,start,end,values,date_filter,data_filter):
	file_name = foldername + "/" + fund_name + file_date + file_type
	wb = xlrd.open_workbook(file_name) 
	sheet = wb.sheet_by_index(0)
	rows = sheet.nrows
	data = list()
	scheme_name = ""
	for i in range(index,rows):
		cells = sheet.row_slice(rowx = i, start_colx = start, end_colx = end)
		if scheme_name == "":
			scheme_name = cells[values[0]].value
		elif scheme_name != "" and cells[values[0]].value != "":
			scheme_name = cells[values[0]].value
		if cells[2].value != "":
			if date_filter == None:
				date = cells[values[1]].value
			else:
				date = xlrd.xldate.xldate_as_datetime(cells[values[1]].value, wb.datemode).strftime('%m-%d-%Y')

			entry = {
				"Name of scheme" : scheme_name,
				"Date" : date,
				"REGULAR_Base_TER_perc" : render_value(inp = cells[values[2]].value, data_filter = data_filter),
				"REGULAR_Addnl_52_6a_b_exp_perc" : render_value(inp = cells[values[3]].value, data_filter = data_filter),
				"REGULAR_Addnl_52_6a_c_exp_perc" : render_value(inp = cells[values[4]].value, data_filter = data_filter),
				"REGULAR_GST_perc" : render_value(inp = cells[values[5]].value, data_filter = data_filter),
				"REGULAR_Total_ter_perc" : render_value(inp = cells[values[6]].value, data_filter = data_filter),
				"DIRECT_Base_TER_perc" : render_value(inp = cells[values[7]].value, data_filter = data_filter),
				"DIRECT_Addnl_52_6a_b_exp_perc" : render_value(inp = cells[values[8]].value, data_filter = data_filter),
				"DIRECT_Addnl_52_6a_c_exp_perc" : render_value(inp = cells[values[9]].value, data_filter = data_filter),
				"DIRECT_GST_perc" : render_value(inp = cells[values[10]].value, data_filter = data_filter),
				"DIRECT_Total_ter_perc" : render_value(inp = cells[values[11]].value, data_filter = data_filter)
			}
						
			data.append(entry)
	return data
def get_data_2(fund_name, file_type,sheet_index,index,start,end,values,name_filter,date_filter,data_filter,check):
	file_name = foldername + "/" + fund_name + file_date + file_type
	data = list()
	wb = xlrd.open_workbook(file_name)
	sheets = wb.nsheets
	for j in range(sheet_index,sheets):
		sheet = wb.sheet_by_index(j)
		rows = sheet.nrows
		scheme_name = ""
		try:
			scheme_row = sheet.row_slice(rowx = values[0], start_colx = start, end_colx = end)
		except:
			continue
		
		if name_filter == None:
			scheme_name = scheme_row[1].value
		else:
			name = scheme_row[0].value
			scheme_name = name[len(name_filter):]

		for i in range(index,rows):
			cells = sheet.row_slice(rowx = i, start_colx = start, end_colx = end)
			if cells[check].value != "":
				if date_filter == None:
					date = cells[values[1]].value
				else:
					date = xlrd.xldate.xldate_as_datetime(cells[values[1]].value, wb.datemode).strftime('%m-%d-%Y')

				entry = {
					"Name of scheme" : scheme_name,
					"Date" : date,
					"REGULAR_Base_TER_perc" : render_value(inp = cells[values[2]].value, data_filter = data_filter),
					"REGULAR_Addnl_52_6a_b_exp_perc" : render_value(inp = cells[values[3]].value, data_filter = data_filter),
					"REGULAR_Addnl_52_6a_c_exp_perc" : render_value(inp = cells[values[4]].value, data_filter = data_filter),
					"REGULAR_GST_perc" : render_value(inp = cells[values[5]].value, data_filter = data_filter),
					"REGULAR_Total_ter_perc" : render_value(inp = cells[values[6]].value, data_filter = data_filter),
					"DIRECT_Base_TER_perc" : render_value(inp = cells[values[7]].value, data_filter = data_filter),
					"DIRECT_Addnl_52_6a_b_exp_perc" : render_value(inp = cells[values[8]].value, data_filter = data_filter),
					"DIRECT_Addnl_52_6a_c_exp_perc" : render_value(inp = cells[values[9]].value, data_filter = data_filter),
					"DIRECT_GST_perc" : render_value(inp = cells[values[10]].value, data_filter = data_filter),
					"DIRECT_Total_ter_perc" : render_value(inp = cells[values[11]].value, data_filter = data_filter)
				}
							
				data.append(entry)
	return data

def get_data_3(fund_name, file_type, index, values, name_filter, r_b_filter, size):
	file_name = foldername + "/" + fund_name + file_date + file_type
	data = list()
	soup = BeautifulSoup(open(file_name),"html.parser")
	rows = soup.findAll("tr")[index:]
	for row in rows:
		col = row.findAll("td")
		if(len(col) == size):
			if r_b_filter == None:
				r_b_ter = col[values[2]].get_text()
			else:
				r_b_ter = col[values[2]].find("span").get_text()
			if name_filter == None:
				scheme = col[values[0]].get_text()
			else:
				scheme = col[values[0]].get_text().replace(u'\xa0', u'')
			entry = {
				"Name of scheme" : scheme,
				"Date" : col[values[1]].get_text(),
				"REGULAR_Base_TER_perc" : r_b_ter,
				"REGULAR_Addnl_52_6a_b_exp_perc" : col[values[3]].get_text(),
				"REGULAR_Addnl_52_6a_c_exp_perc" : col[values[4]].get_text(),
				"REGULAR_GST_perc" : col[values[5]].get_text(),
				"REGULAR_Total_ter_perc" : col[values[6]].get_text(),
				"DIRECT_Base_TER_perc" : col[values[7]].get_text(),
				"DIRECT_Addnl_52_6a_b_exp_perc" : col[values[8]].get_text(),
				"DIRECT_Addnl_52_6a_c_exp_perc" : col[values[9]].get_text(),
				"DIRECT_GST_perc" : col[values[10]].get_text(),
				"DIRECT_Total_ter_perc" : col[values[11]].get_text()
			}
			data.append(entry)
	
	return data
		
def get_data_4(fund_name, file_type, index, index2, values, filter):
	file_name = foldername + "/" + fund_name + file_date + file_type
	data = list()
	first = list()
	second = list()
	if fund_name == "axis":
		soup = BeautifulSoup(open(file_name),"html.parser")
	else:
		soup = BeautifulSoup(open(file_name, encoding = "utf-8"),"html.parser")
	rows = soup.findAll("tr")[index:]
	for row in rows:
		cols = row.findAll("td")
		plan = cols[index2].get_text()

		if plan.find("Regular") != -1:
			entry = {
				"Name of scheme" : cols[values[0]].get_text(),
				"Date" : cols[values[1]].get_text(),
				"REGULAR_Base_TER_perc" : cols[values[2]].get_text() if filter == None else cols[values[2]].get_text()[:-1],
				"REGULAR_Addnl_52_6a_b_exp_perc" : cols[values[3]].get_text() if filter == None else cols[values[3]].get_text()[:-1],
				"REGULAR_Addnl_52_6a_c_exp_perc" : cols[values[4]].get_text() if filter == None else cols[values[4]].get_text()[:-1],
				"REGULAR_GST_perc" : cols[values[5]].get_text() if filter == None else cols[values[5]].get_text()[:-1],
				"REGULAR_Total_ter_perc" : cols[values[6]].get_text() if filter == None else cols[values[6]].get_text()[:-1],
			}
			first.append(entry)
		else:
			entry = {
				"DIRECT_Base_TER_perc" : cols[values[7]].get_text() if filter == None else cols[values[7]].get_text()[:-1],
				"DIRECT_Addnl_52_6a_b_exp_perc" : cols[values[8]].get_text() if filter == None else cols[values[8]].get_text()[:-1],
				"DIRECT_Addnl_52_6a_c_exp_perc" : cols[values[9]].get_text() if filter == None else cols[values[9]].get_text()[:-1],
				"DIRECT_GST_perc" : cols[values[10]].get_text() if filter == None else cols[values[10]].get_text()[:-1],
				"DIRECT_Total_ter_perc" : cols[values[11]].get_text() if filter == None else cols[values[11]].get_text()[:-1]
			}
			second.append(entry)
	for i in range(len(second)):
		d = dict(list(first[i].items())+list(second[i].items()))
		data.append(d)

	return data	

get_data(fund_name = "adityabirla", file_type = ".xlsx", index = 2, start = 0, end = 12, values = data_values.aditya_values , date_filter = None, data_filter = None)