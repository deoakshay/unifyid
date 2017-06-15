from urllib2 import Request, urlopen, URLError
request=("https://www.random.org/integers/?num=10&min=1&max=1000&col=2&base=10&format=plain&rnd=new")

try:
	response=urlopen(request)
	tp=response.read()
	print tp
except URLError,e:
	print e
