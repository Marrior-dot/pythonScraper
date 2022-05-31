import gspread

#Conexão com a conta de serviço do Google Cloud
sa = gspread.service_account()
#Seleção da tabela do googleSheets
sh = sa.open('titulo_subtitulo')

wks = sh.worksheet("Sheet1")

print(wks.row_count)

