#先判断是否run
#run  执行runmethod
#再判断是否有数据依赖
#有数据依赖 则通过caseid 返回依赖接口的响应数据  执行依赖运行方式(把header cookies写入json文件)
from util import  M_Excel
from data import  get_data
from  base import  runmethod,dependmethod
from util import  M_Json,M_headers,M_email,M_assert
import json
import requests
import string


class run():
    def __init__(self):
        self.Massert=M_assert.Myassert()
        self.email=M_email.Mail()
        self.excel=M_Excel.Myxlrd()
        self.data=get_data.Getdata()
        self.json_data=M_Json.dispose_json()
        self.headers_cookies=M_headers.Headers_Cookies_Dict()
        self.run_case=runmethod.RunMethod()
        self.run_depend_case=dependmethod.rundependmethod()
        self.header_dict = {}
        self.cookies_dict = {}

    def run_all_case(self):
        count = self.data.case_lines()
        for i in range(1,count):
            is_run = self.data.case_run(i)
            case_id = self.data.case_id(i)
            url = self.data.case_url(i)
            method = self.data.case_method(i)
            header = self.data.case_header(i)
            cookies = self.data.case_cookies(i)
            case_denpend = self.data.case_depend(i)
            data_depend = self.data.Case_Jsonpath(i)
            key = self.data.Case_Data_key(i)
            case_data = self.data.case_data(i)
            execpt = self.data.get_expect_data_sql(i)
            if is_run:
                res=self.run_case.get_run(method=method,url=url,data=case_data,headers=header,cookies=cookies)
                # print(self.json_data.json_(res.json()))
                if case_denpend:
                    res=self.run_depend_case.run_depend_case(i)
                    num=self.run_depend_case.depend_case_row(i)
                    depend_case_id = self.data.case_id(num)
                    # 把被依赖用例的header写入字典
                    self.header_dict[depend_case_id] = dict(res.headers)
                    # 把被依赖用例的cookies写入字典
                    cookie = requests.utils.dict_from_cookiejar(res.cookies)
                    self.cookies_dict[depend_case_id] = dict(cookie)
                    if self.Massert.is_contain(execpt,res.json()):
                        self.data.write_result(i, "pass")
                    else:
                        self.data.write_result(i, "False")

        self.json_data.write_data("../dataconfig/cookies.json", self.cookies_dict)
        self.json_data.write_data("../dataconfig/headers.json", self.header_dict)
        # self.email.Send_Mail("报告")


if __name__ == '__main__':
    a=run()
    a.run_all_case()
