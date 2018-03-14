import urllib2
import urllib
url = "http://www.stackoverflow.com/"
values = {}
values["q"] = "foo"
data = urllib.urlencode(values)
request = urllib2.Request(url + "search" +"?"+ data)
response = urllib2.urlopen(request)
html = response.read()
print html
