import ezsheets

#Uploads an Excel file
s_s_2 = ezsheets.upload('trf_soc.xlsx')

#Downloads with another name
s_s_2.downloadAsExcel('trf_sor.xlsx')

#Downloads with the same name
s_s_2.downloadAsODS()
