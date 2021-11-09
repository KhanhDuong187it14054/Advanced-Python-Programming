import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print (response.status_code)
print (response.json())

#200
# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
