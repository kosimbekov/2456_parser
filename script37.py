import requests

URL = 'https://jsonplaceholder.typicode.com'

posts_response = requests.get(f"{URL}/posts")
print(posts_response )
