import urllib.request
import json
try:
    url_google = urllib.request.urlopen("http://www.google.com/")


    jsonString = url_google.readline()
    print(jsonString)
    d = jsonString.decode()
    jsonFile = open("Lab08/data.html", "w")
    jsonFile.write(d)
    jsonFile.close()
except urllib.error.URLError as e:
    print("Error: ", e.reason)