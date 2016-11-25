#!/usr/bin/python
import site
site.addsitedir('/Users/trishalkumar/anaconda2/lib/python2.7/site-packages')
from yahoo_finance import Currency
import time
from threading import Thread
import time

import sys
import site
site.addsitedir('/Users/trishalkumar/anaconda2/lib/python2.7/site-packages')
import cgi, cgitb


cgitb.enable()
print("Content-type: text/html\r\n\r\n")


form = cgi.FieldStorage()
currency_traded = int(form.getvalue('user_value'))

#print (currency_traded)


usd_eur,usd_jpy,usd_gbp,usd_chf,usd_cad,usd_aud,usd_hkd,usd_inr,usd_sgd = (0,)*9
eur_usd,eur_jpy,eur_gbp,eur_chf,eur_cad,eur_aud,eur_hkd,eur_inr,eur_sgd = (0,)*9
jpy_usd,jpy_eur,jpy_gbp,jpy_chf,jpy_cad,jpy_aud,jpy_hkd,jpy_inr,jpy_sgd = (0,)*9
gbp_usd,gbp_eur,gbp_jpy,gbp_chf,gbp_cad,gbp_aud,gbp_hkd,gbp_inr,gbp_sgd = (0,)*9
chf_usd,chf_eur,chf_jpy,chf_gbp,chf_cad,chf_aud,chf_hkd,chf_inr,chf_sgd = (0,)*9
cad_usd,cad_eur,cad_jpy,cad_gbp,cad_chf,cad_aud,cad_hkd,cad_inr,cad_sgd = (0,)*9
aud_usd,aud_eur,aud_jpy,aud_gbp,aud_chf,aud_cad,aud_hkd,aud_inr,aud_sgd = (0,)*9
hkd_usd,hkd_eur,hkd_jpy,hkd_gbp,hkd_chf,hkd_cad,hkd_aud,hkd_inr,hkd_sgd = (0,)*9
inr_usd,inr_eur,inr_jpy,inr_gbp,inr_chf,inr_cad,inr_aud,inr_hkd,inr_sgd = (0,)*9
sgd_usd,sgd_eur,sgd_jpy,sgd_gbp,sgd_chf,sgd_cad,sgd_aud,sgd_hkd,sgd_inr = (0,)*9 

mapping = { 1 : 'US Dollar : USD' , 2 : 'European : EUR' , 3 : 'Japanese : YEN',
			4 : 'British Pound : GBP' , 5 : 'Switzerland Franc : CHF', 6 : 'Canadian Dollar : CAD',
			7 : 'Australian Dollar : AUD', 8 : 'Hong Kong Dollar : HKD', 9 :'Indian Rupee : INR',
			10 : 'Singapore Dollar : SGD'}

# currency_traded = 1000 			

def usd():
	global usd_eur, eur_usd, usd_jpy, jpy_usd, chf_usd, usd_chf, cad_usd, usd_cad, gbp_usd, usd_gbp

	eur_usd = float(Currency('EURUSD').get_rate())
 	usd_eur = 1/eur_usd

	jpy_usd = float(Currency('JPYUSD').get_rate())
	usd_jpy = 1/jpy_usd

	gbp_usd = float(Currency('GBPUSD').get_rate())
	usd_gbp = 1/gbp_usd

	chf_usd = float(Currency('CHFUSD').get_rate())
	usd_chf = 1/chf_usd

	cad_usd = float(Currency('CADUSD').get_rate())
	usd_cad = 1/cad_usd


def eur():
	global jpy_eur, eur_jpy, gbp_eur, eur_gbp, chf_eur, eur_chf, cad_eur, eur_cad, aud_eur, eur_aud

	jpy_eur = float(Currency('JPYEUR').get_rate())
	eur_jpy = 1/jpy_eur

	gbp_eur = float(Currency('GBPEUR').get_rate())
	eur_gbp = 1/gbp_eur

	chf_eur = float(Currency('CHFEUR').get_rate())
	eur_chf = 1/chf_eur

	cad_eur = float(Currency('CADEUR').get_rate())
	eur_cad = 1/cad_eur

	aud_eur = float(Currency('AUDEUR').get_rate())
	eur_aud = 1/aud_eur

def jpy():
	global chf_jpy, jpy_chf, cad_jpy, jpy_cad, aud_jpy, jpy_aud, hkd_jpy, jpy_hkd, inr_jpy, jpy_inr
	
	chf_jpy = float(Currency('CHFJPY').get_rate())
	jpy_chf = 1/chf_jpy

	cad_jpy = float(Currency('CADJPY').get_rate())
	jpy_cad = 1/cad_jpy

	aud_jpy = float(Currency('AUDJPY').get_rate())
	jpy_aud = 1/aud_jpy

	hkd_jpy = float(Currency('HKDJPY').get_rate())
	jpy_hkd = 1/hkd_jpy

	inr_jpy = float(Currency('INRJPY').get_rate())
	jpy_inr = 1/inr_jpy


def gbp():
	global jpy_gbp, gbp_jpy, chf_gbp, gbp_chf, cad_gbp, gbp_cad, aud_gbp, gbp_aud, hkd_gbp, gbp_hkd
	
	jpy_gbp = float(Currency('JPYGBP').get_rate())
	gbp_jpy = 1/jpy_gbp

	chf_gbp = float(Currency('CHFGBP').get_rate())
	gbp_chf = 1/chf_gbp

	cad_gbp = float(Currency('CADGBP').get_rate())
	gbp_cad = 1/cad_gbp

	aud_gbp = float(Currency('AUDGBP').get_rate())
	gbp_aud = 1/aud_gbp

	hkd_gbp = float(Currency('HKDGBP').get_rate())
	gbp_hkd = 1/hkd_gbp
	
def chf():
	global cad_chf, chf_cad, aud_chf, chf_aud, hkd_chf, chf_hkd, inr_chf, chf_inr, sgd_chf, chf_sgd
	
	cad_chf = float(Currency('CADCHF').get_rate())
	chf_cad = 1/cad_chf

	aud_chf = float(Currency('AUDCHF').get_rate())
	chf_aud = 1/aud_chf

	hkd_chf = float(Currency('HKDCHF').get_rate())
	chf_hkd = 1/hkd_chf

	inr_chf = float(Currency('INRCHF').get_rate())
	chf_inr = 1/inr_chf

	sgd_chf = float(Currency('SGDCHF').get_rate())
	chf_sgd = 1/sgd_chf

def cad():
	global aud_cad, cad_aud, hkd_cad, cad_hkd, inr_cad, cad_inr, sgd_cad, cad_sgd, sgd_jpy, jpy_sgd
	
	aud_cad = float(Currency('AUDCAD').get_rate())
	cad_aud = 1/aud_cad

	hkd_cad = float(Currency('HKDCAD').get_rate())
	cad_hkd = 1/hkd_cad

	inr_cad = float(Currency('INRCAD').get_rate())
	cad_inr = 1/inr_cad

	sgd_cad = float(Currency('SGDCAD').get_rate())
	cad_sgd = 1/sgd_cad

	sgd_jpy = float(Currency('SGDJPY').get_rate())
	jpy_sgd = 1/sgd_jpy

def aud():
	global hkd_aud, aud_hkd, inr_aud, aud_inr, sgd_aud, aud_sgd, inr_gbp, gbp_inr, sgd_gbp, gbp_sgd
	
	hkd_aud = float(Currency('HKDAUD').get_rate())
	aud_hkd = 1/hkd_aud

	inr_aud = float(Currency('INRAUD').get_rate())
	aud_inr = 1/inr_aud

	sgd_aud = float(Currency('SGDAUD').get_rate())
	aud_sgd = 1/sgd_aud

	inr_gbp = float(Currency('INRGBP').get_rate())
	gbp_inr = 1/inr_gbp

	sgd_gbp = float(Currency('SGDGBP').get_rate())
	gbp_sgd = 1/sgd_gbp

def hkd():
	global inr_hkd, hkd_inr, sgd_hkd, hkd_sgd, hkd_eur, eur_hkd, inr_eur, eur_inr, sgd_eur, eur_sgd
	
	inr_hkd = float(Currency('INRHKD').get_rate())
	hkd_inr = 1/inr_hkd

	sgd_hkd = float(Currency('SGDHKD').get_rate())
	hkd_sgd = 1/sgd_hkd

	hkd_eur = float(Currency('HKDEUR').get_rate())
	eur_hkd = 1/hkd_eur

	inr_eur = float(Currency('INREUR').get_rate())
	eur_inr = 1/inr_eur

	sgd_eur = float(Currency('SGDEUR').get_rate())
	eur_sgd = 1/sgd_eur

def inr():
	global sgd_inr, inr_sgd, aud_usd, usd_aud, hkd_usd, usd_hkd, inr_usd, usd_inr, sgd_usd, usd_sgd
	
	sgd_inr = float(Currency('SGDINR').get_rate())
	inr_sgd = 1/sgd_inr

	aud_usd = float(Currency('AUDUSD').get_rate())
	usd_aud = 1/aud_usd

	hkd_usd = float(Currency('HKDUSD').get_rate())
	usd_hkd = 1/hkd_usd

	inr_usd = float(Currency('INRUSD').get_rate())
	usd_inr = 1/inr_usd

	sgd_usd = float(Currency('SGDUSD').get_rate())
	usd_sgd = 1/sgd_usd

def cycle():
	for i in range(0,len(conversion_list)):
		for j in range(0,len(conversion_list)):
			if(i!=j):
				conv = conversion_list[i][j]
				detected(conv,i,j)

cycle_detected=[]
#Stores the cycle in the form of  ( curr1 ---> curr2 ---> curr3 ----> curr1 ) + associated profit

def detected(rate,i,j):
	for k in range(0,len(conversion_list)):
		if(k != i and k != j):
			conversion = conversion_list[i][k] * conversion_list[k][j]
			if((conversion - rate) > 0.6):
				#profit =  (currency_traded * conversion * conversion_list[j][i]) - currency_traded
				#profit = round(profit, 3)
				#print (profit)

				#original_curr_profit = "profit in term of original currency: "
				#original_curr_profit += str(profit) 

				profit_in_USD = 'Profit in Dollar ($) : '
				dollar_profit = (currency_traded * conversion * conversion_list[j][i] * conversion_list[i][1] ) - (currency_traded * conversion_list[i][1])
				dollar_profit = round(dollar_profit, 3)
				profit_in_USD += str(dollar_profit)

				l=[]

				l.append(mapping[i+1])
				l.append(mapping[k+1])
				l.append(mapping[j+1])

				#l.append(original_curr_profit)
				l.append(profit_in_USD)

				cycle_detected.append(l)


def fetch():
	threads = []

	thread1 = Thread(target = usd)
	#thread1.start()
	threads.append(thread1)
		
	thread2 = Thread(target = eur)
	#thread2.start()
	threads.append(thread2)

	thread3 = Thread(target = jpy)
	#thread3.start()
	threads.append(thread3)

	thread4 = Thread(target = gbp)
	#thread4.start()
	threads.append(thread4)

	thread5 = Thread(target = chf)
	#thread5.start()
	threads.append(thread5)

	thread6 = Thread(target = cad)
	#thread6.start()
	threads.append(thread6)

	thread7 = Thread(target = aud)
	#thread7.start()
	threads.append(thread7)

	thread8 = Thread(target = hkd)
	#thread8.start()
	threads.append(thread8)

	thread9 = Thread(target = inr)
	#thread9.start()
	threads.append(thread9)

	for t in threads:
		t.start()
		#time.sleep(0.1)

	for t in threads:
		t.join()


if __name__ == '__main__':

	start_time = time.time()

 	

	fetch()

	#Create Matrix
	conversion_list = [[1,usd_eur,usd_jpy,usd_gbp,usd_chf,usd_cad,usd_aud,usd_hkd,usd_inr,usd_sgd],
					   [eur_usd,1,eur_jpy,eur_gbp,eur_chf,eur_cad,eur_aud,eur_hkd,eur_inr,eur_sgd],
					   [jpy_usd,jpy_eur,1,jpy_gbp,jpy_chf,jpy_cad,jpy_aud,jpy_hkd,jpy_inr,jpy_sgd],
					   [gbp_usd,gbp_eur,gbp_jpy,1,gbp_chf,gbp_cad,gbp_aud,gbp_hkd,gbp_inr,gbp_sgd],
					   [chf_usd,chf_eur,chf_jpy,chf_gbp,1,chf_cad,chf_aud,chf_hkd,chf_inr,chf_sgd],
					   [cad_usd,cad_eur,cad_jpy,cad_gbp,cad_chf,1,cad_aud,cad_hkd,cad_inr,cad_sgd],
					   [aud_usd,aud_eur,aud_jpy,aud_gbp,aud_chf,aud_cad,1,aud_hkd,aud_inr,aud_sgd],
					   [hkd_usd,hkd_eur,hkd_jpy,hkd_gbp,hkd_chf,hkd_cad,hkd_aud,1,hkd_inr,hkd_sgd],
					   [inr_usd,inr_eur,inr_jpy,inr_gbp,inr_chf,inr_cad,inr_aud,inr_hkd,1,inr_sgd],
					   [sgd_usd,sgd_eur,sgd_jpy,sgd_gbp,sgd_chf,sgd_cad,sgd_aud,sgd_hkd,sgd_inr,1]]
	test_bit = 1
	for i in range(0,len(conversion_list)):
		for j in range(0,len(conversion_list)):
			if conversion_list[i][j] == 0:
				test_bit = 0
				
				break
	if test_bit == 0:
		print "<html><body><p style='font-size: 48;font-style: bold; color: white;'>Unstable connection. Retry</p></body></html>"
		print "</br>"*1000

	#print ( conversion_list )	

	cycle()
	print "<html><head><title>Cycle Detection</title>"
	print "<style> #cycles{ font-size: 26px; font-style: bold;} body{background-color: black; color: white;}</style>"
	print "</head><body>"

	print ("<p style='font-size: 20px; font-style: bold;'>Possible combinations for an investment of USD %d </p></br>" %currency_traded)
	print "<div id = 'cycles'>"

	#print(cycle_detected)
	for c in range(1, len(cycle_detected) + 1 ):
		print("Cycle : %d " %c+"")
		for ci in range(0,3):
			print("%s --->" %cycle_detected[c-1][ci])
		print(cycle_detected[c-1][3])
		print("</br>")
		print("</br>")
	print "</div>"

	print ("<p style='font-size: 22px; color: white;'>Time taken to detect the cycle is : --- %s seconds --- </p>"% round((time.time() - start_time), 4))
	print "</body></html>"


