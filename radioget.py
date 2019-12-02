# importing the requests library 
import requests 
import json
import random

def runRadio():  
	# defining the api-endpoints
	API_ENDPOINT = "http://www.radio-browser.info/webservice/json/stations"
	API_ENDPOINT_2 = "http://www.radio-browser.info/webservice/json/stats"
	  
	# data to be sent to api 
	data = {'api_paste_format':'python'} 
	  
	# sending post request and saving response as response object 
	r = requests.post(url = API_ENDPOINT, data = data)
	t = requests.post(url = API_ENDPOINT_2, data = data) 
	  
	# extracting response text  
	json_text = r.text 
	json_text_2 = t.text
	results_dict = json.loads(json_text)
	results_dict_2 = json.loads(json_text_2)

	#choose random station
	numStations = results_dict_2["stations"]
	randNum = random.randrange(numStations)
	url = results_dict[randNum]["url"]
	name = results_dict[randNum]["name"]
	country = results_dict[randNum]["country"]
	language = results_dict[randNum]["language"]
	print(url, name, country, language)

	return url, name, country, language