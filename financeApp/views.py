from django.shortcuts import render
from alpha_vantage.timeseries import TimeSeries
import pandas as pd; import numpy as np
from django_pandas.io import read_frame


def home(request):

	key = '2ff9638945msha6d129df62431d4p1f1adejsn540a73c51b98'
	ts = TimeSeries(key,output_format='pandas', indexing_type='date')

	if request.method == 'GET':
		return render(request, 'Mainpage/home.html')
	else:
		ticker = request.POST.get('Ticker')
		prices = ts.get_daily(symbol = ticker)[0].reset_index()
		prices.columns = ['date','open','high','low','close','volume']
		prices['Change'] = round((prices.close/prices.open - 1)*100,3)
		prices['Ticker'] = ticker
		data = [prices.iloc[row].to_dict() for row in range(10)]
		# data=[]
		# for key in prices.keys():
		# 	x =  { "date": key,"open":prices[key]['1. open'],"close":prices[key]['4. close']}
		# 	data.append(x)

		context = { 'prices':data }
		return render(request, 'Mainpage/home.html',context)

# def home(request):
#     return render(request, 'Mainpage/home.html',context)