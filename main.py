import data_values
import json_parser
import json_parser_individuals
import json
import values_cleaner
import datetime

today = datetime.datetime.now()
file_date = "_" + str(today.day) + "_" + str(today.month) + "_" + str(today.year)

foldername = file_date[1:]

data = dict()

try:
	data["adityabirla"] = values_cleaner.clean_aditya(json_parser.get_data(fund_name = "adityabirla", file_type = ".xlsx", index = 2, start = 0, end = 12, values = data_values.aditya_values , date_filter = None, data_filter = None))
except:
	data["adityabirla"] = []

try:
	data["axis"] = values_cleaner.clean_axis(json_parser.get_data_4(fund_name = "axis", file_type = ".html", index = 1, index2 = 0, values = data_values.axis_values, filter = "yes"))
except:
	data["axis"] = []

try:
	data["baroda"] = values_cleaner.clean_baroda(json_parser.get_data_3(fund_name = "baroda", file_type = ".xls", index = 5, values = data_values.baroda_values, name_filter = None, r_b_filter = "yes", size = 12))
except:
	data["baroda"] = []

try:	
	data["bnpparibas"] = values_cleaner.clean_bnp(json_parser.get_data(fund_name = "bnpparibas", file_type = ".xls", index = 2, start = 0, end = 12, values = data_values.bnp_values , date_filter = None, data_filter = None))
except:
	data["bnpparibas"] = []

try:	
	data["boi"] = json_parser_individuals.get_data_boi()
except:
	data["boi"] = []

try:	
	data["canara"] = values_cleaner.clean_canara(json_parser.get_data_3(fund_name = "canara", file_type = ".html", index = 4, values = data_values.canara_values, name_filter = None, r_b_filter = "yes", size = 12))
except:
	data["canara"] = []

try:	
	data["dhfl"] = json_parser.get_data_2(fund_name = "dhfl", file_type = ".xlsx", sheet_index = 3,index = 5,start = 0,end = 11,values = data_values.dhfl_values, name_filter = None, date_filter = "yes", data_filter = "yes", check = 1)
except:
	data["dhfl"] = []

try:	
	data["dsp"] = json_parser.get_data(fund_name = "dsp", file_type = ".xlsx", index = 4, start = 0, end = 12, values = data_values.dsp_values, date_filter = "yes", data_filter = None)
except:
	data["dsp"] = []

try:	
	data["edelweiss"] = values_cleaner.clean_edelweiss(json_parser.get_data_3(fund_name = "edelweiss", file_type = ".xls", index = 2, values = data_values.edelweiss_values, name_filter = "yes", r_b_filter = None, size = 12))
except:
	data["edelweiss"] = []

try:	
	data["essel"] = values_cleaner.clean_essel(json_parser.get_data(fund_name = "essel", file_type = ".xls", index = 3, start = 0, end = 12, values = data_values.essel_values , date_filter = None, data_filter = None))
except:
	data["essel"] = []

try:	
	data["franklintempleton"] = json_parser.get_data(fund_name = "franklintempleton", file_type = ".xlsx", index = 9, start = 0, end = 12, values = data_values.franklin_values, date_filter = "yes", data_filter = "yes")
except:
	data["franklintempleton"] = []

try:	
	data["hdfc"] = json_parser.get_data(fund_name = "hdfc", file_type = ".xls", index = 2, start = 0, end = 12, values = data_values.hdfc_values, date_filter = "yes", data_filter = None)
except:
	data["hdfc"] = []
try:
	data["hsbc"] = json_parser_individuals.get_data_hsbc()
except:
	data["hsbc"] = []


try:	
	data["icici"] = values_cleaner.clean_icici(json_parser.get_data(fund_name = "icici", file_type = ".xlsx", index = 3, start = 0, end = 12, values = data_values.icici_values, date_filter = None, data_filter = None))
except:
	data["icici"] = []

try:	
	data["idbi"] = values_cleaner.clean_idbi(json_parser.get_data(fund_name = "idbi", file_type = ".xls", index = 2, start = 1, end = 13, values = data_values.idbi_values, date_filter = "yes", data_filter = None))
except:
	data["idbi"] = []

try:	
	data["idfc"] = json_parser.get_data(fund_name = "idfc", file_type = ".xlsx", index = 2, start = 1, end = 13, values = data_values.idfc_values, date_filter = "yes", data_filter = "yes")
except:
	data["idfc"] = []

try:	
	data["iifcl"] = values_cleaner.clean_iifcl(json_parser.get_data_2(fund_name = "iifcl", file_type = ".xlsx", sheet_index = 0,index = 5,start = 1,end = 12,values = data_values.iifcl_values, name_filter = "Name of Scheme: ", date_filter = "yes", data_filter = None, check = 1))
except:
	data["iifcl"] = []

try:	
	data["iifl"] = json_parser.get_data(fund_name = "iifl", file_type = ".xls", index = 2, start = 0, end = 12, values = data_values.iifl_values, date_filter = "yes", data_filter = "yes")
except:
	data["iifl"] = []

try:	
	data["ilfs"] = values_cleaner.clean_ilfs(json_parser.get_data_2(fund_name = "ilfs", file_type = ".xls", sheet_index = 0,index = 5,start = 0,end = 11,values = data_values.ilfs_values, name_filter = "Name of Scheme: ", date_filter = "yes", data_filter = None, check = 1))
except:
	data["ilfs"] = []

try:	
	data["indiabulls"] = values_cleaner.clean_indiabulls(json_parser.get_data_2(fund_name = "indiabulls", file_type = ".xls", sheet_index = 0,index = 3,start = 0,end = 11,values = data_values.indiabulls_values, name_filter = "Name of Scheme: ", date_filter = "yes", data_filter = "yes", check = 1))
except:
	data["indiabulls"] = []

try:	
	data["invesco"] = json_parser.get_data(fund_name = "invesco", file_type = ".xls", index = 2, start = 0, end = 12, values = data_values.invesco_values, date_filter = "yes", data_filter = "yes")
except:
	data["invesco"] = []

try:	
	data["jmfinancial"] = json_parser.get_data_2(fund_name = "jmfinancial", file_type = ".xlsx", sheet_index = 0,index = 6,start = 0,end = 11,values = data_values.jm_values, name_filter = "Name of Scheme: ", date_filter = "yes", data_filter = None, check = 1)
except:
	data["jmfinancial"] = []

try:	
	data["kotak"] = json_parser.get_data_2(fund_name = "kotak", file_type = ".xls", sheet_index = 1,index = 5,start = 0,end = 11,values = data_values.kotak_values, name_filter = None, date_filter = "yes", data_filter = None, check = 1)
except:
	data["kotak"] = []

try:	
	data["ltfs"] = json_parser.get_data(fund_name = "ltfs", file_type = ".xlsx", index = 2, start = 0, end = 12, values = data_values.ltfs_values, date_filter = "yes", data_filter = "yes")
except:
	data["ltfs"] = []

try:	
	data["lic"] = values_cleaner.clean_lic(json_parser.get_data_4(fund_name = "lic", file_type = ".html", index = 2, index2 = 2, values = data_values.lic_values, filter = None))
except:
	data["lic"] = []

try:	
	data["mahindra"] = values_cleaner.clean_mahindra(json_parser.get_data(fund_name = "mahindra", file_type = ".xlsx", index = 2, start = 0, end = 12, values = data_values.mahindra_values, date_filter = None, data_filter = None))
except:
	data["mahindra"] = []

try:	
	data["mirae"] = json_parser.get_data(fund_name = "mirae", file_type = ".xls", index = 2, start = 0, end = 12, values = data_values.mirae_values, date_filter = "yes", data_filter = "yes")
except:
	data["mirae"] = []

try:	
	data["motilal"] = values_cleaner.clean_motilal(json_parser.get_data_3(fund_name = "motilal", file_type = ".xls", index = 2, values = data_values.motilal_values, name_filter = None,r_b_filter = None, size = 12))
except:
	data["motilal"] = []

try:	
	data["ppfas"] = json_parser_individuals.get_data_ppfas()
except:
	data["ppfas"] = []

try:	
	data["principal"] = json_parser.get_data_2(fund_name = "principal", file_type = ".xls", sheet_index = 0,index = 4,start = 0,end = 11,values = data_values.principal_values, name_filter = "Name of Scheme: ", date_filter = "yes", data_filter = None, check = 1)
except:
	data["principal"] = []

try:	
	data["quant"] = json_parser.get_data(fund_name = "quant", file_type = ".xls", index = 1, start = 0, end = 12, values = data_values.quant_values, date_filter = "yes", data_filter = None)
except:
	data["quant"] = []

try:	
	data["quantum"] = values_cleaner.clean_quantum(json_parser.get_data_2(fund_name = "quantum", file_type = ".xlsx", sheet_index = 0,index = 4,start = 0,end = 11,values = data_values.quantum_values, name_filter = "Name of Scheme : ", date_filter = None, data_filter = None, check = 1))
except:
	data["quantum"] = []

try:	
	data["reliance"] = values_cleaner.clean_reliance(json_parser.get_data(fund_name = "reliance", file_type = ".xlsx", index = 2, start = 0, end = 12, values = data_values.reliance_values , date_filter = "yes", data_filter = None))
except:
	data["reliance"] = []

try:	
	data["sahara"] = json_parser_individuals.get_data_sahara()
except:
	data["sahara"] = []

try:	
	data["sbi"] = values_cleaner.clean_sbi(json_parser.get_data(fund_name = "sbi", file_type = ".xlsx", index = 2, start = 0, end = 12, values = data_values.sbi_values, date_filter = "yes", data_filter = None))
except:
	data["sbi"] = []

try:	
	data["shriram"] = json_parser_individuals.get_data_shriram()
except:
	data["shriram"] = []

try:	
	data["sundaram"] = values_cleaner.clean_sundaram(json_parser_individuals.get_data_sundaram())
except:
	data["sundaram"] = []

try:	
	data["tata"] = values_cleaner.clean_tata(json_parser.get_data(fund_name = "tata", file_type = ".xls", index = 8, start = 0, end = 12, values = data_values.tata_values , date_filter = "yes", data_filter = None))
except:
	data["tata"] = []

try:	
	data["taurus"] = values_cleaner.clean_taurus(json_parser.get_data_3(fund_name = "taurus", file_type = ".html", index = 3, values = data_values.taurus_values, name_filter = None, r_b_filter = None, size = 13))
except:
	data["taurus"] = []

try:	
	data["union"] = values_cleaner.clean_union(json_parser.get_data_2(fund_name = "union", file_type = ".xlsx", sheet_index = 0,index = 6,start = 0,end = 11,values = data_values.union_values, name_filter = None, date_filter = "yes", data_filter = None, check = 0))
except:
	data["union"] = []

try:	
	data["uti"] = values_cleaner.clean_uti(json_parser.get_data(fund_name = "uti", file_type = ".xlsx", index = 3, start = 0, end = 12, values = data_values.uti_values, date_filter = None, data_filter = None))
except:
	data["uti"] = []

file_name = foldername + "/" + "data" + file_date + ".json"
with open(file_name,"w") as f:
	json.dump(data, f,indent = 4)
