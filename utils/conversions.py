import urllib2
import json

#uses the yahoo! api for getting current exchange rate. Takes a CNY price and returns USD
#Note: if theres and error in the api request (404, etc.) this function returns 0.
def cny_to_usd(cny):
	try:
		site = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDCNY%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
		response = urllib2.urlopen(site)
		raw_info = json.loads(response.read())
		rate = float(raw_info['query']['results']['rate']['Rate'])
		usd = round(cny/rate,3)

	#if an error is raised, return 0 for price
	except urllib2.HTTPError, e:
		usd = 0
	return usd
