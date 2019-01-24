#!/usr/bin/python

import urllib2
import json

req = urllib2.Request("https://gist.githubusercontent.com/ab9-er/27a903b8636e745fb820a7d310177c46/raw/9315383f0a0f8da2f0931ba69ab7be2d1f7b95b5/world_universities_and_domains.json")
opener = urllib2.build_opener()
f = opener.open(req)
result = json.loads(f.read())
n = 0

try:
	for x in result:
		try:
			print "Web Pages: "
			print result[n]['web_pages']
			print "Name: "
			print result[n]['name']
			print "Alpha Two Code: "
			print result[n]['alpha_two_code']
			print "State / Province: "
			print result[n]['state-province']
			print "Domains: "
			print result[n]['domains']
			print "Country: "
			print result[n]['country'] + "\n"
			n = n + 1
		except (TypeError, NameError): 
			print ("Please check the syntax")
		except(ValueError):
			print ("Please check your value")
except (RuntimeError, RuntimeWarning):
	print("There could be one or more run time errors or warnings")
except:
	print("Unexpected error: ", sys.exc_info()[0])