import urllib.request

url_google = urllib.request.urlopen("http://www.google.com/")
print(url_google.read())
print(url_google.info())
print(url_google.getcode()) # trả về status - 200
print(url_google.geturl())  # trả về url