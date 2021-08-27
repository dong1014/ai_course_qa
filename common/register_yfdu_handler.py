from request_handler import RequestsHandler

class register_yfdu:

    # cookies = {
    #     'ai_persistent': 'mxWNFVxQA/sg4IvxQAobPd8HFsKQaR16CEl/HxE/YSgXXTH2xEgELZT9ADId2xUu72WZLho3X24Chbcp5jqxWw==',
    #     'persistent': 'rSQImtBmEnpj9yekUpoAlkMZ0WTZGlJuBcKndxKtYvjSF2gA/5VLwGIV3Fe96QOdWKJPPsDOsWnuM0nPLr6iIQ=='
    # }
    def register_success(self):
        url = "https://aries.yuanfudao.biz/aries-auth/iphone/register/yfdu?_productId=1901&av=5&platform=14.4.2&version=1.6.0&_hostProductId=1901"

        payload = "AI_YFD=tBqg3G8400ZQINsDj8Ra2EXj4fH4d4rhGvCynLUITI5unYOavg/N2zRYnrESmroc%0D%0AAd5r0cS4C7gF3qU%2BWwAi3fegaca%2BlcbCLHaX1JPFYGW2oPkhdRabA0cUo%2B/OB14k%0D%0AC1axOIBZi78fjRQcYbHpp2kqlAU6TVRkZYxnIkJ/igk%3D&AI_YFD_INFO=%7B%22id%22%3A%22plZvy2buQcxdmr2Pc31%5C/pzqVVn3wmQiDIN0W3hs3hATLJ1xX87EBaVFwoV5Y103m%5Cr%5CnqXsq967dCigpX5lXKTiVCkiAI2zG7gVcwNB20CJqKAdJbixc2BQPOshv1qA7Ms3w%5Cr%5Cn16WI75jkB87g1yCXNUQzu95N%5C/aAjzVF3c1QVoPoMAzw%3D%22%2C%22model%22%3A%22iPhone%2011%22%7D"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'User-Agent': 'Aries/1.6.0 (com.fenbi.ariesinhouse; build:52; iOS 14.4.2) Alamofire/5.4.3',
            'cookie': 'ai_persistent=mxWNFVxQA/sg4IvxQAobPd8HFsKQaR16CEl/HxE/YSgXXTH2xEgELZT9ADId2xUu72WZLho3X24Chbcp5jqxWw==; persistent=rSQImtBmEnpj9yekUpoAlkMZ0WTZGlJuBcKndxKtYvjSF2gA/5VLwGIV3Fe96QOdWKJPPsDOsWnuM0nPLr6iIQ=='
        }
        req = RequestsHandler()
        res = req.visit(url,method='post', data=payload, headers=headers).json
        print(res.cookies)

if __name__ == '__main__':
    r=register_yfdu()
    r.register_success()


