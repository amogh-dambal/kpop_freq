from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def fetch(url):
	try:
		with closing(get(url, stream=True)) as rsp:
			if validate(rsp):
				return rsp.content
			else:
				return None
	except RequestException as e:
		log_error('Error during requests to {0}: {1}'.format(url, str(e)))
		return None


'''
Ensures that the given response is a 
valid HTML response and contains
HTML text to be parsed
'''


def validate(rsp):
	content_type = rsp.content['Content-Type'].lower()
	return (
		rsp.status_code == 200
		and content_type is not None
		and content_type.find('html') > 1
	)

'''
Basic logging of errors to separate files
'''

def log_error(error):
	with open("log/errors.txt", 'wb') as f:
		f.write(error)
		return True


