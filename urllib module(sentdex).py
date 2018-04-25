import urllib.request
import urllib.parse

#a = urllib.request.urlopen('https://www.google.com')
#print(a.read())

#url = 'http://www.pythonprogramming.net'
#value = {'q':'basic'}

#data = urllib.parse.urlencode(value)
#data= data.encode('utf-8')
#req = urllib.request.Request(url,data)
#resp = urllib.request.urlopen(req)
#respData = resp.read()

#print(respData)

try:
    url = 'https://www.androidpolice.com/search?q=text'
    headers = {}
    headers['User-Agent']= 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withheaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))