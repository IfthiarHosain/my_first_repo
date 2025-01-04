import requests
url="https://www.google.co.uk/"
response=requests.get(url)
if response.status_code ==200:
    print(response.text[:500])
else:
    print(f"failed to fetch website.status code: {response.status_code}")