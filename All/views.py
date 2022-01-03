from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
import requests
from bs4 import BeautifulSoup
import datetime

def getliste(year , month , day):
	req = requests.get("https://www.filgoal.com/matches/?date={}-{}-{}".format(str(year),str(month),str(day)))
	soup = BeautifulSoup(req.text, 'html.parser')
	mydivs = soup.find("div" , id='match-list-viewer')
	soup1 = BeautifulSoup(str(mydivs), 'html.parser')
	mydivs1 = soup1.find_all("div" , class_='mc-block')
	AllMatch = []
	if len(mydivs1) == 0:
		AllMatch = []
		return AllMatch
	else:
		for i in mydivs1:
			soup2 = BeautifulSoup(str(i), 'html.parser')
			mydivs2 = soup2.find_all("span")
			D = []
			D.append(str(mydivs2[0].text))
			soup2 = BeautifulSoup(str(i), 'html.parser')
			mydivs2 = soup2.find_all("div" , class_='cin_cntnr')
			for j in mydivs2:
				M = []
				soupmyf = BeautifulSoup(str(j) , 'html.parser')
				myf = soupmyf.find('div' , class_='f')
				M.append(str(myf.strong.text))
				M.append(str(myf.b.text))
				M.append('https:' + str(myf.img.get('data-src')))
				soupmym = BeautifulSoup(str(j) , 'html.parser')
				mym = soupmym.find('div' , class_='m')
				M.append(str(mym.span.text))
				soupmys = BeautifulSoup(str(j) , 'html.parser')
				mys = soupmys.find('div' , class_='s')
				M.append(str(mys.strong.text))
				M.append(str(mys.b.text))
				M.append('https:' + str(mys.img.get('data-src')))
				D.append(M)
			AllMatch.append(D)
		return AllMatch

def index(request):
	AllMatch = getliste(datetime.date.today().year , datetime.date.today().month , datetime.date.today().day)
	return render(request , 'All/index.html' , {'AllMatch':AllMatch})

def tomorrow(request):
	AllMatch = getliste(datetime.date.today().year , datetime.date.today().month , datetime.date.today().day + 1)
	return render(request , 'All/tomorrow.html' , {'AllMatch':AllMatch})

def yesterday(request):
	AllMatch = getliste(datetime.date.today().year , datetime.date.today().month , datetime.date.today().day - 1)
	return render(request , 'All/yesterday.html' , {'AllMatch':AllMatch})

def error_404_view(request , exception):
	return redirect('index')
