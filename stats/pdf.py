import requests
import sys
from PyPDF2 import PdfFileReader
import os

def headers():
	print(os.getcwd())
	print(50*"="+"\nC19 Karnataka Script v0.1")
	print(50*"="+'\n\n')

def getData(date):
	
	url = 'https://covid19.karnataka.gov.in/storage/pdf-files/Media-Bulletin/'+date+"-2020%20HMB%20English.pdf"

	if not os.path.exists(os.path.join(os.getcwd()+f"/stats/data/{date}.pdf")):
		print("Getting Data...")
		req = requests.get(url)

		if req.status_code == 200:
			f = open(os.getcwd()+"/stats/data/"+date+'.pdf','w+b')
			f.write(req.content)
			f.close()
			print("Done, Parsing...")
		else:
			print(f'\n[{req.status_code}] Something went wrong :(\nPlease Check the date')
			sys.exit(1)
	
	with open(os.getcwd()+"/stats/data/"+date+'.pdf', 'rb') as f:
	    pdf = PdfFileReader(f)
	    # get the first page
	    page = pdf.getPage(1)
	    text = page.extractText()
	    arr = []
	    for i in text.strip().split():
	    	if len(arr):
	    		if arr[-1].isalpha() and i.isalpha():
	    			arr[-1]+=i
	    		else:
	    			arr.append(i.strip())
	    	else:
	    		arr.append(i.strip())
	    print("District",7*" ","Positives")
	    for i in range(arr.index('BengaluruUrban'),arr.index('Total')+1):
	    	if arr[i].isalpha() and arr[i+1].isdigit():
	    		print(arr[i],(15-len(arr[i]))*" ",arr[i+1])
	    sys.exit(0)