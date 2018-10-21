# Requests: HTTP library for Python
# Requests is the only Non-GMO HTTP library for Python, safe for human consumption
# http://docs.python-requests.org/en/latest/index.html

################################

# 1) simple request
import requests
r = requests.get('https://github.com/leolanese', auth=('laneseleo@gmail.com', ''))
r.status_code

r.headers['content-type']
'application/json; charset=utf8'

r.encoding

r.text

r.json()

r.headers # Response Headers

r.status_code == requests.codes.ok

r.headers['Content-Type'] # Response Headers

r.headers.get('content-type')


# 2) JSON Response Content
import requests
r = requests.get('https://api.github.com/events')
r.json()

# 3) More complicated POST requests
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.post("https://httpbin.org/post", data=payload)
>>> print(r.text)


4) Cookies
url = 'http://mimecast.com'
r = requests.get(url)
r.cookies





http://docs.python-requests.org/en/latest/index.html
