import requests

class RequestsHandler:

    def visit(url,method, params = None, data= None, json= None, headers= None):
        res = requests.request(url,method,params= params,data = data,json = json,headers = headers)
        try:
            #返回json结果
            return res.json
        except Exception:
            return "not json"

    def close_session(self):
        self.session.close()
