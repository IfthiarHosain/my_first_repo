import requests
url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
if response.status_code ==200:
    users=response.json()
    for user in users:
        print(f"Name:user{["Name"]}, email:user{["email"]}")
    else:
        print(f"failed to fetch fata.status code. {response.status_code}")