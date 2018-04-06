import requests
import json

class RunMethod():


    def get_main(self,url,data=None,headers=None,cookies=None):
        res = None
        if data and  headers and  cookies:
            res=requests.get(url,data=data,headers=headers,cookies=cookies,verify=False)
        elif data and headers and not cookies:
            res = requests.get(url, data=data, headers=headers,verify=False)
        elif data and cookies and not headers :
            res = requests.get(url, data=data, cookies=cookies,verify=False)
        elif headers and cookies and not data:
            res = requests.get(url,headers=headers,cookies=cookies,verify=False)
        elif data and not  headers and not cookies:
            res = requests.get(url,data=data,verify=False)
        elif headers and not  data and not cookies:
            res = requests.get(url, headers=headers,verify=False)
        elif  cookies and not  data and not headers:
            res = requests.get(url, cookies=cookies,verify=False)
        return res

    def post_main(self,url,data=None,headers=None,cookies=None):
        res = None
        if data and  headers and  cookies:
            res=requests.post(url,data=data,headers=headers,cookies=cookies,verify=False)
        elif data and headers and not cookies:
            res = requests.post(url, data=data, headers=headers,verify=False)
        elif data and cookies and not headers :
            res = requests.post(url, data=data, cookies=cookies,verify=False)
        elif headers and cookies and not data:
            res = requests.post(url,headers=headers,cookies=cookies,verify=False)
        elif data and not  headers and not cookies:
            res = requests.post(url,data=data,verify=False)
        elif headers and not  data and not cookies:
            res = requests.post(url, headers=headers,verify=False)
        elif  cookies and not  data and not headers:
            res = requests.post(url, cookies=cookies,verify=False)
        return res

    def get_run(self,method,url,data=None,headers=None,cookies=None):
        # 禁用安全请求警告
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        res1 = None
        if method=="get":
            res1=self.get_main(url,data,headers,cookies)
        else:
            res1 = self.post_main(url,data,headers,cookies)
        return res1

if __name__ == '__main__':
    url="http://www.httpbin.org/post"
    method="get"
    data={"comments": "",
    "custemail": "",
    "custname": "111",
    "custtel": "",
    "delivery": ""}
    headers={ "User-Agent": "Mozilla/7.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    cookies={"name":"allen"}
    a=RunMethod()
    b=a.get_run(method="post",url=url,data=data,headers=headers)
    # c=json.dumps(b,sort_keys=True, indent=4, ensure_ascii=False)
    print(b.json())


