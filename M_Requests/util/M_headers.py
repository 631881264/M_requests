import  json
import requests
from  util import  M_Json
from util import  M_Excel
from data import  get_data
from base import  dependmethod


class Headers_Cookies_Dict():
    """把被依赖用例响应header 和 cookiesx写到字典"""
    def __init__(self):
        self.json=M_Json.dispose_json()

        self.data=get_data.Getdata()
        self.header_dict={}
        self.cookies_dict={}


    def Get_All_Header(self, row, r):
        """把header写入一个大字典"""
        case_id=self.data.case_id(row)
        self.header_dict[case_id]=dict(r.headers)

    def Get_All_Cookies(self, row, r):
        """"把cookies写入一个大字典"""
        case_id = self.data.case_id(row)
        cookie=requests.utils.dict_from_cookiejar(r.cookies)
        self.cookies_dict[case_id]=dict(cookie)

if __name__ == '__main__':
    r=requests.get("http://www.baidu.com")
    a=Headers_Cookies_Dict()
    case_id=["case_01","case_02"]

    a.Get_All_Cookies(2, r=r)
    print(a.cookies_dict)

    a.json.write_data("../dataconfig/cookies.json", a.cookies_dict)

