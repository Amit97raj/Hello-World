from urllib.request import urlopen
import json

postLink = "https://my-json-server.typicode.com/typicode/demo/posts"
commentsLink = "https://my-json-server.typicode.com/typicode/demo/comments"

p = urlopen(postLink)
postObject = json.loads(p.read())
# postObject = p.read().decode('utf-8')

c= urlopen(commentsLink)
# commentObject = c.read().decode('utf-8')
commentObject = json.loads(c.read())

# comments = commentObject.split('\n')

for i in commentObject:
    a = i.get('postId')
    for j in postObject:
        if a == j.get("id"):
            j[f'comment{i.get("id")}'] = i



print(postObject)

p.close()
c.close()



#2nd question Answer
import urllib3
import json

http = urllib3.PoolManager()
namesList = []
for i in range(1,13):
    link = f"https://reqres.in/api/users?page={i}"
    req = http.request('GET',link)
    f = req.data
    # f = http.request.urlopen(req)
    
    data = json.loads(f)
    data = data["data"]
    if data:
        for j in data:
            namesList.append(str(f"{j.get('first_name')} {j.get('last_name')}"))

    req.close()





# print(namesList)

print(f"The tolal number of users is : {len(namesList)}")

