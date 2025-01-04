import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title": "new post" ,
    "body" : "This is the content of the post",
    "userID": 1
}
response=requests.post(url,json=data)
if response.status_code==201:
    print("post created successfully")
    print("response:", response.json())
else:
    print(f"failed to create a post.Status code: {response.status_code}")