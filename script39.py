import requests

URL = "https://jsonplaceholder.typicode.com/photos"
response = requests.get(URL)
photos = response.json()
print(len(photos))
print(photos[0])

URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(URL)
posts = response.json()
print(posts[0])

URL = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(URL)
comments = response.json()
print(comments[0])

