import requests
url="https://www.v2ex.com/api/nodes/show.json"
data={"name":"java"}
r=requests.get(url,data=data)
b=r.json()
import  json
c=json.loads(b)
print(c)