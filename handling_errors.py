import requests
url="https://jsonplaceholder.typicode.com/unknown"
response=requests.get(url)
if response.status_code==200:
    print("success:", response.json())
elif response.status_code==404:
    print("error resource not found (404)")
elif response.status_code==500:
    print("internal server error (500)")
else:
    print(f"unexpected error,status code: {response.status_code}")
