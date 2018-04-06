from util import M_Excel,M_Pysqldb,M_Json
from data import data_config


class Getdata():
    def __init__(self):
        self.excel=M_Excel.Myxlrd()
        self.op_mysql = M_Pysqldb.MyDb("mysql",style="1")
        self.my_json=M_Json.dispose_json()

# 去获取excel行数,就是我们的case个数
    def case_lines(self):
        return self.excel.Get_All_Lines()

    def case_id(self,row):
        """用例id"""
        col = int(data_config.id())
        caseid = self.excel.Get_Only_Value(row, col)
        return caseid
    def case_url(self,row):
        """用例url"""
        col = int(data_config.url())
        url = self.excel.Get_Only_Value(row, col)
        return url

    def case_run(self,row):
        """用例运行"""
        flag = None
        col = int(data_config.run())
        run_model = self.excel.Get_Only_Value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def case_method(self, row):
        """请求方式"""
        col = int(data_config.requests_way())
        request_method = self.excel.Get_Only_Value(row, col)
        return request_method


    def case_header(self, row):
        """用例header"""
        col = int(data_config.header())
        header = self.excel.Get_Only_Value(row, col)
        if header == "yes":
            return header
        else:
            return None

    def case_cookies(self,row):
        """用例cookies"""
        col=int(data_config.cookies())
        cookies = self.excel.Get_Only_Value(row, col)
        if cookies =="yes":
            return cookies
        else:
            return None
    def case_depend(self, row):
        """用例依赖"""
        col = int(data_config.case_depend())
        depend_case_id = self.excel.Get_Only_Value(row, col)
        if depend_case_id != "":
            return depend_case_id
        else:
            return None


    def Case_Jsonpath(self, row):
        """获取jsonpath"""
        col = int(data_config.data_depen())
        data = self.excel.Get_Only_Value(row, col)
        if data == "":
            return None
        else:
            return data
            # 获取数据依赖字段

    def Case_Data_key(self, row):
        """key"""
        col = int(data_config.field_depen())
        key = self.excel.Get_Only_Value(row, col)
        flag=None
        if key == "":
            flag = None
        else:
            flag= key
        return flag

    def case_data(self, row):
        """用例data数据"""
        col = int(data_config.data())
        key = self.excel.Get_Only_Value(row, col)
        # 读取data.json文件
        flag=None
        if key == '':
            flag=None
        else:
            data=self.my_json.read_json_file("../dataconfig/data.json")[key]
            flag= data
        return flag


    def case_expcet_data(self, row):
        """预期结果"""
        col = int(data_config.expect())
        expect = self.excel.Get_Only_Value(row, col)
        if expect == '':
            return None
        return expect

    # 通过sql获取预期结果
    def get_expcet_data_for_mysql(self, row):
        """预期结果"""
        sql = self.case_expcet_data(row)
        self.op_mysql.execute_sql(sql)
        res=self.op_mysql.get_one()
        return res
    def get_expect_data_sql(self,row):
        """预期结果"""
        flag=None
        try:
            flag= self.get_expcet_data_for_mysql(row)
        except:
            flag= self.case_expcet_data(row)
        return flag



    def write_result(self, row, value):
        """写入实际结果"""
        col = int(data_config.result())
        self.excel.Write_Value(row, col, value)


if __name__ == '__main__':
    a=Getdata()
    run = a.Case_Data_key(1)
    print(run)




    # 实际结果