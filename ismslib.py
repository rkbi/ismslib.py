import requests, urllib, time
import config

# Configuration Values
USERNAME = config.config['username']
PASSWD = config.config['password']
SID = config.config['sid']

def sendSMSWithGet(msisdn, body):
	params = getParams(msisdn, body)
	response = requests.get('https://sms.sslwireless.com/pushapi/dynamic/server.php', params=params)
	return response.text

def sendSMSWithPost(msisdn, body):
	params = getParams(msisdn, body)
	response = requests.post('https://sms.sslwireless.com/pushapi/dynamic/server.php', params=params)
	return response.text

def getParams(msisdn, body):
	params = {
		'user': USERNAME,
		'pass': PASSWD,
		'sid': SID,
		'sms': body,
		'msisdn': msisdn,
		'csmsid': str(round(time.time() * 1000)),
	}
	urllib.parse.urlencode(params)
	return params
