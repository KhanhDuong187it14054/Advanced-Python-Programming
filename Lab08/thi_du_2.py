import urllib.request

url_google = urllib.request.urlopen('https://www.python.org/search/?q=urlopen&submit=')
print(url_google.read())
# Lấy nội dung kết quả tìm kiếm