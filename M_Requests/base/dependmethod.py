from data import  get_data
from util import  M_Excel,M_headers
from base import runmethod
from jsonpath_rw import jsonpath,parse



class rundependmethod():
    """row 依赖用例的行 叫做A
    对于要被执行的被依赖用例 叫做B
    要获取的数据有
    B:url method 原始data header cookies    (通过row处理得到的行)
    A:key值 数据依赖字段 新的data"""
    def __init__(self):
        self.data=get_data.Getdata()
        self.excel=M_Excel.Myxlrd()
        self.all_case_id = self.excel.Get_Cols_Data()
        self.my_headers=M_headers.Headers_Cookies_Dict()
        self.header_dict = {}
        self.cookies_dict = {}

    def depend_case_row(self,row):
        """根据row 获取依赖case的行数"""
        depend_caseid=self.data.case_depend(row)
        for i in range(len(self.all_case_id)):
            num=0
            if self.all_case_id[i]==depend_caseid:
                return i
            num = num+1

    def get_data_for_key(self, row,r):
        """对响应体做解析 返回一个具体值"""
        # 获取jsonpath表达式
        depend_jsonpath = self.data.Case_Jsonpath(row)
        json_exe = parse(depend_jsonpath)
        madle = json_exe.find(r.json())
        return [math.value for math in madle][0]

    def change_data_value(self, row):
        """修改原始data数据,并写入"""
        # 通过caes_id 去读取data.json   然后修改数据依赖字段的value
        data_depend = self.data.Case_Data_key(row)
        # 根据row 获取case_id
        case_id = self.data.case_id(row)
        # 读取data.json文件
        data_json_file = M_Json.dispose_json().read_json_file("../dataconfig/data.json")
        # 通过case_id读取数据
        data_json_file[case_id][data_depend] = new_data
        self.datajson.write_data("../dataconfig/data.json", data_json_file)

    def run_depend_case(self, row):
        """
        row:最后执行for循环中的row
        depend_row:指的是被依赖case的行号
        """
        depend_row=self.depend_case_row(row)
        depend_id=self.data.case_id(depend_row)
        depend_method = self.data.case_method(depend_row)
        depend_url=self.data.case_url(depend_row)
        depend_data=self.data.case_data(depend_row)
        depend_header=self.data.case_header(depend_row)
        depend_cookies=self.data.case_cookies(depend_row)
        r=runmethod.RunMethod().get_run(method=depend_method,url=depend_url,data=depend_data,headers=depend_header,cookies=depend_cookies)
        # 通过jsonpath 对响应体做解析
        new_value=self.get_data_for_key(row,r=r.json())
        self.change_data_value(row)
        return r

if __name__ == '__main__':
    rundependmethod().run_depend_case(2)

