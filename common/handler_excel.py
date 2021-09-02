#coding = uft-8
import openpyxl
import os

base_path = os.path.dirname(os.getcwd())

class HandlerExcel:
    def __init__(self,path):
        self.path = path


    def open_excel(self):
        open_excel = openpyxl.load_workbook(base_path + self.path)
        return open_excel
    # 获取测试用例所在工作表
    def get_sheet(self,name):
        sheet_name = self.open_excel()
        return sheet_name[name]

    def get_value(self,name):
        sheet = self.get_sheet(name)
        # 表头列表
        title = []
        #将每行数据写入list中
        data = []
        rows = list(sheet.rows)
        # 将第一行的数据写入title
        for value in rows[0]:
            title.append(value)

        # 将每行数据写入data中
        for row in rows[1:]:
            row_data ={}
            for key,cell in enumerate(row):
                row_data[title[key]]=cell.value
            data.append(row_data)

        return data


    def get_excel(self):
        ws = self.get_sheet()
        data = ws.cell(1,1).value
        print(data)

if __name__ == "__main__":
    Handler = HandlerExcel('/case/case.xlsx')
    print(Handler.get_value('sale_info'))





