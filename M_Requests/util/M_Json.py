import json
from jsonpath_rw import jsonpath,parse
class dispose_json():

    def json_(self,data):
        return json.dumps(data,ensure_ascii=False)

    def write_data(self,file_name,data):
        """写入json文件"""
        with open(file_name,'w',encoding="utf-8") as fp:
            fp.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False) + "\n")


    def read_json_file(self, file_name):
        """读取json"""
        with open(file_name,"r",encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    #把case_id连同响应一起写入json文件
    def write_data_caseid(self,file_name,data,case_id):

        data_caseid={}
        data_caseid[case_id]=data
        data_json=json.dumps(data_caseid,sort_keys=True,indent=4,ensure_ascii=False)
        with open(file_name,'w',encoding="utf-8") as fp:
            fp.write(data_json)

if __name__ == '__main__':
    a=dispose_json()
    b=a.read_json_file("../dataconfig/data.json")
    b["case_003"]["id"]=700
    a.write_data("../dataconfig/data.json",b)

