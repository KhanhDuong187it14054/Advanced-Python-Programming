import requests
API_KEY = 'AIzaSyBe_HPZ_PyMp6dJMY2l_Zlb4cnDzyFSQ7w'
video_id = '7cmvABXyUC0'
url = "https://www.googleapis.com/youtube/v3/video?id="+video_id+"&part=statistics&key="+API_KEY
response = requests.get(url).json()
print(response)