months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

def clean_value(inp):
	inp = inp*100
	inp ="{0:.2f}".format(inp)
	return inp

def clean_aditya(data):
	for item in data:
		actual_date = item["Date"].split("-")
		day = actual_date[0]
		month = months.index(actual_date[1]) + 1
		year = actual_date[2]
		item["Date"] = str(month) + "-" + day + "-" + year
	return data


def clean_axis(data):
	for item in data:
		actual_date = item["Date"].split("-")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data
 
def clean_baroda(data):
	for item in data:
		actual_date = item["Date"].split("/")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data

def clean_bnp(data):
	for item in data:
		actual_date = item["Date"].split("/")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data

def clean_canara(data):
	for item in data:
		actual_date = item["Date"].split("/")
		day = actual_date[1]
		month = actual_date[0]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data


def clean_edelweiss(data):
	for item in data:
		actual_date = item["Date"].split(" ")
		day = actual_date[0]
		month = months.index(actual_date[1].upper()) + 1
		year = actual_date[2]
		item["Date"] = str(month) + "-" + day + "-" + year
	return data

def clean_essel(data):
	for item in data:
		actual_date = item["Date"].split("/")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
		item["REGULAR_Base_TER_perc"] = "{0:.2f}".format(item["REGULAR_Base_TER_perc"])
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = "{0:.2f}".format(item["REGULAR_Addnl_52_6a_b_exp_perc"])
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = "{0:.2f}".format(item["REGULAR_Addnl_52_6a_c_exp_perc"])
		item["REGULAR_GST_perc"] = "{0:.2f}".format(item["REGULAR_GST_perc"])
		item["REGULAR_Total_ter_perc"] = "{0:.2f}".format(item["REGULAR_Total_ter_perc"])
		item["DIRECT_Base_TER_perc"] = "{0:.2f}".format(item["DIRECT_Base_TER_perc"])
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = "{0:.2f}".format(item["DIRECT_Addnl_52_6a_b_exp_perc"])
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = "{0:.2f}".format(item["DIRECT_Addnl_52_6a_c_exp_perc"])
		item["DIRECT_GST_perc"] = "{0:.2f}".format(item["DIRECT_GST_perc"])
		item["DIRECT_Total_ter_perc"] = "{0:.2f}".format(item["DIRECT_Total_ter_perc"])
	return data

def clean_icici(data):
	for item in data:
		actual_date = item["Date"].split("/")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
		item["REGULAR_Base_TER_perc"] = item["REGULAR_Base_TER_perc"][:-1]
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = item["REGULAR_Addnl_52_6a_b_exp_perc"][:-1]
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = item["REGULAR_Addnl_52_6a_c_exp_perc"][:-1]
		item["REGULAR_GST_perc"] = item["REGULAR_GST_perc"][:-1]
		item["REGULAR_Total_ter_perc"] = item["REGULAR_Total_ter_perc"][:-1]
		item["DIRECT_Base_TER_perc"] = item["DIRECT_Base_TER_perc"][:-1]
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = item["DIRECT_Addnl_52_6a_b_exp_perc"][:-1]
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = item["DIRECT_Addnl_52_6a_c_exp_perc"][:-1]
		item["DIRECT_GST_perc"] = item["DIRECT_GST_perc"][:-1]
		item["DIRECT_Total_ter_perc"] = item["DIRECT_Total_ter_perc"][:-1]
	return data

def clean_idbi(data):
	for item in data:
		item["REGULAR_Total_ter_perc"] = "{0:.2f}".format(item["REGULAR_Total_ter_perc"])
	return data

def clean_iifcl(data):
	for item in data:
		item["REGULAR_Base_TER_perc"] = "" if item["REGULAR_Base_TER_perc"] == "N/A" else item["REGULAR_Base_TER_perc"]
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = "" if item["REGULAR_Addnl_52_6a_b_exp_perc"] == "N/A" else item["REGULAR_Addnl_52_6a_b_exp_perc"]
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = "" if item["REGULAR_Addnl_52_6a_c_exp_perc"] == "N/A" else item["REGULAR_Addnl_52_6a_c_exp_perc"]
		item["REGULAR_GST_perc"] = "" if item["REGULAR_GST_perc"] == "N/A" else item["REGULAR_GST_perc"]
		item["REGULAR_Total_ter_perc"] = "" if item["REGULAR_Total_ter_perc"] == "N/A" else item["REGULAR_Total_ter_perc"]
		item["DIRECT_Base_TER_perc"] = "" if item["DIRECT_Base_TER_perc"] == "N/A" else item["DIRECT_Base_TER_perc"]
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = "" if item["DIRECT_Addnl_52_6a_b_exp_perc"] == "N/A" else item["DIRECT_Addnl_52_6a_b_exp_perc"]
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = "" if item["DIRECT_Addnl_52_6a_c_exp_perc"] == "N/A" else item["DIRECT_Addnl_52_6a_c_exp_perc"]
		item["DIRECT_GST_perc"] = "" if item["DIRECT_GST_perc"] == "N/A" else item["DIRECT_GST_perc"]
		item["DIRECT_Total_ter_perc"] = "" if item["DIRECT_Total_ter_perc"] == "N/A" else item["DIRECT_Total_ter_perc"]
	return data

def clean_iifcl(data):
	for item in data:
		item["REGULAR_Base_TER_perc"] = "" if item["REGULAR_Base_TER_perc"] == "N/A" else item["REGULAR_Base_TER_perc"]
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = "" if item["REGULAR_Addnl_52_6a_b_exp_perc"] == "N/A" else item["REGULAR_Addnl_52_6a_b_exp_perc"]
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = "" if item["REGULAR_Addnl_52_6a_c_exp_perc"] == "N/A" else item["REGULAR_Addnl_52_6a_c_exp_perc"]
		item["REGULAR_GST_perc"] = "" if item["REGULAR_GST_perc"] == "N/A" else item["REGULAR_GST_perc"]
		item["REGULAR_Total_ter_perc"] = "" if item["REGULAR_Total_ter_perc"] == "N/A" else item["REGULAR_Total_ter_perc"]
		item["DIRECT_Base_TER_perc"] = "" if item["DIRECT_Base_TER_perc"] == "N/A" else item["DIRECT_Base_TER_perc"]
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = "" if item["DIRECT_Addnl_52_6a_b_exp_perc"] == "N/A" else item["DIRECT_Addnl_52_6a_b_exp_perc"]
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = "" if item["DIRECT_Addnl_52_6a_c_exp_perc"] == "N/A" else item["DIRECT_Addnl_52_6a_c_exp_perc"]
		item["DIRECT_GST_perc"] = "" if item["DIRECT_GST_perc"] == "N/A" else item["DIRECT_GST_perc"]
		item["DIRECT_Total_ter_perc"] = "" if item["DIRECT_Total_ter_perc"] == "N/A" else item["DIRECT_Total_ter_perc"]
	return data
def clean_ilfs(data):
	for item in data:
		item["REGULAR_Base_TER_perc"] = "" if item["REGULAR_Base_TER_perc"] == "N.A." else item["REGULAR_Base_TER_perc"]
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = "" if item["REGULAR_Addnl_52_6a_b_exp_perc"] == "N.A." else item["REGULAR_Addnl_52_6a_b_exp_perc"]
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = "" if item["REGULAR_Addnl_52_6a_c_exp_perc"] == "N.A." else item["REGULAR_Addnl_52_6a_c_exp_perc"]
		item["REGULAR_GST_perc"] = clean_value(item["REGULAR_GST_perc"])
		item["REGULAR_Total_ter_perc"] = clean_value(item["REGULAR_Total_ter_perc"])
		item["DIRECT_Base_TER_perc"] = "" if item["DIRECT_Base_TER_perc"] == "N.A." else item["DIRECT_Base_TER_perc"]
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = "" if item["DIRECT_Addnl_52_6a_b_exp_perc"] == "N.A." else item["DIRECT_Addnl_52_6a_b_exp_perc"]
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = "" if item["DIRECT_Addnl_52_6a_c_exp_perc"] == "N.A." else item["DIRECT_Addnl_52_6a_c_exp_perc"]
		item["DIRECT_GST_perc"] = clean_value(item["DIRECT_GST_perc"])
		item["DIRECT_Total_ter_perc"] = clean_value(item["DIRECT_Total_ter_perc"])
	return data

def clean_indiabulls(data):
	for item in data:
		item["Name of scheme"] = item["Name of scheme"][:-1]
	return data

def clean_lic(data):
	for item in data:
		actual_date = item["Date"].split("-")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data

def clean_mahindra(data):
	for item in data:
		actual_date = item["Date"].split("-")
		day = actual_date[0]
		month = months.index(actual_date[1].upper()) + 1
		year = actual_date[2]
		item["Date"] = str(month) + "-" + day + "-" + year
		item["REGULAR_Base_TER_perc"] = item["REGULAR_Base_TER_perc"][:-1]
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = item["REGULAR_Addnl_52_6a_b_exp_perc"][:-1]
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = item["REGULAR_Addnl_52_6a_c_exp_perc"][:-1]
		item["REGULAR_GST_perc"] = item["REGULAR_GST_perc"][:-1]
		item["REGULAR_Total_ter_perc"] = item["REGULAR_Total_ter_perc"][:-1]
		item["DIRECT_Base_TER_perc"] = item["DIRECT_Base_TER_perc"][:-1]
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = item["DIRECT_Addnl_52_6a_b_exp_perc"][:-1]
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = item["DIRECT_Addnl_52_6a_c_exp_perc"][:-1]
		item["DIRECT_GST_perc"] = item["DIRECT_GST_perc"][:-1]
		item["DIRECT_Total_ter_perc"] = item["DIRECT_Total_ter_perc"][:-1]
	return data

def clean_motilal(data):
	for item in data:
		actual_date = item["Date"].split("-")
		day = actual_date[0]
		month = months.index(actual_date[1].upper()) + 1
		year = actual_date[2]
		item["Date"] = str(month) + "-" + day + "-" + year
	return data

def clean_quantum(data):
	for item in data:
		actual_date = item["Date"].split("-")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data

def clean_reliance(data):
	for item in data:
		item["REGULAR_Base_TER_perc"] = item["REGULAR_Base_TER_perc"] * 100
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = item["REGULAR_Addnl_52_6a_b_exp_perc"] * 100
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = item["REGULAR_Addnl_52_6a_c_exp_perc"] * 100
		item["REGULAR_GST_perc"] = item["REGULAR_GST_perc"] * 100
		item["REGULAR_Total_ter_perc"] = item["REGULAR_Total_ter_perc"] * 100
		item["DIRECT_Base_TER_perc"] = item["DIRECT_Base_TER_perc"] * 100
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = item["DIRECT_Addnl_52_6a_b_exp_perc"] * 100
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = item["DIRECT_Addnl_52_6a_c_exp_perc"] * 100
		item["DIRECT_GST_perc"] = item["DIRECT_GST_perc"] * 100
		item["DIRECT_Total_ter_perc"] = item["DIRECT_Total_ter_perc"] * 100
	return data

def clean_sbi(data):
	for item in data:
		item["REGULAR_GST_perc"] = "{0:.2f}".format(item["REGULAR_GST_perc"])
	return data

def clean_sundaram(data):
	for item in data:
		actual_date = item["Date"].split("-")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data

def clean_tata(data):
	for item in data:
		item["REGULAR_Base_TER_perc"] = "{0:.2f}".format(item["REGULAR_Base_TER_perc"])
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = "{0:.2f}".format(item["REGULAR_Addnl_52_6a_b_exp_perc"])
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = "{0:.2f}".format(item["REGULAR_Addnl_52_6a_c_exp_perc"])
		item["REGULAR_GST_perc"] = "{0:.2f}".format(item["REGULAR_GST_perc"])
		item["REGULAR_Total_ter_perc"] = "{0:.2f}".format(item["REGULAR_Total_ter_perc"])
		item["DIRECT_Base_TER_perc"] = "{0:.2f}".format(item["DIRECT_Base_TER_perc"])
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = "{0:.2f}".format(item["DIRECT_Addnl_52_6a_b_exp_perc"])
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = "{0:.2f}".format(item["DIRECT_Addnl_52_6a_c_exp_perc"])
		item["DIRECT_GST_perc"] = "{0:.2f}".format(item["DIRECT_GST_perc"])
		item["DIRECT_Total_ter_perc"] = "{0:.2f}".format(item["DIRECT_Total_ter_perc"])
	return data

def clean_taurus(data):
	for item in data:
		actual_date = item["Date"].split("/")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data

def clean_union(data):
	for item in data:
		item["REGULAR_Base_TER_perc"] = "{0:.2f}".format(item["REGULAR_Base_TER_perc"])
		item["REGULAR_Addnl_52_6a_b_exp_perc"] = "{0:.2f}".format(item["REGULAR_Addnl_52_6a_b_exp_perc"])
		item["REGULAR_Addnl_52_6a_c_exp_perc"] = "{0:.2f}".format(item["REGULAR_Addnl_52_6a_c_exp_perc"])
		item["REGULAR_GST_perc"] = "{0:.2f}".format(item["REGULAR_GST_perc"])
		item["REGULAR_Total_ter_perc"] = "{0:.2f}".format(item["REGULAR_Total_ter_perc"])
		item["DIRECT_Base_TER_perc"] = "{0:.2f}".format(item["DIRECT_Base_TER_perc"])
		item["DIRECT_Addnl_52_6a_b_exp_perc"] = "{0:.2f}".format(item["DIRECT_Addnl_52_6a_b_exp_perc"])
		item["DIRECT_Addnl_52_6a_c_exp_perc"] = "{0:.2f}".format(item["DIRECT_Addnl_52_6a_c_exp_perc"])
		item["DIRECT_GST_perc"] = "{0:.2f}".format(item["DIRECT_GST_perc"])
		item["DIRECT_Total_ter_perc"] = "{0:.2f}".format(item["DIRECT_Total_ter_perc"])
	return data

def clean_uti(data):
	for item in data:
		actual_date = item["Date"].split("/")
		day = actual_date[0]
		month = actual_date[1]
		year = actual_date[2]
		item["Date"] = month + "-" + day + "-" + year
	return data