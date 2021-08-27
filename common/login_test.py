import requests

class devices:
  url = "https://aries.yuanfudao.biz/aries-auth/android/register/yfdu"
  params = "_productId=1911&_hostProductId=1911&platform=android29&version=1.6.0&av=5"
  payload = "AI_YFD=ODHQAV54xzDMciV9%2B91j0LLf%2BmFFqzc7ucDI467FCRiJH7qBD%2BJkinMG4eA11pWthYZqQQVZ12tsg7AWeAl5sODLGp7EraJyzFhyz8GL%2FZlZPaeHawm%2BMOfbzU28ccSNUawfUX3HEba6WTZfVsEpgE8vOUqhqHvF8DEa5FMSHHw%3D&AI_YFD_INFO=%7B%22id%22%3A%22nvU9S9QE%2BwYfyYWFqEFpAW7aBiQmSaPXRJQP7AhSHiZ3Xso7km5HpAqi8N1NJMQe82e2hqSi2BNwK%5C%2FIUV2fL2bGJmdmWsIDqFIZ2NqHXgoQpU2GU7PF9UpOG%5C%2FEJE6drpwqs9deUfeFtTU8Ci7yaA%5C%2F85xh9GKA6cr7sbuRY4g4vQ%3D%22%2C%22brand%22%3A%22HUAWEI%22%2C%22device%22%3A%22HWNOH%22%2C%22model%22%3A%22NOH-AL00%22%2C%22sdk%22%3A29%2C%22host%22%3A%22cn-east-hcd-4a-568589d2e1625990501471-6f96f8789b-d4p5s%22%2C%22rom%22%3A%22NOH-AL00%202.0.0.138%28C00E130R8P2%29%22%2C%22release%22%3A%2210%22%7D"
  headers = {
    'Host': 'aries.yuanfudao.biz',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Aries/1.6.0 (HUAWEINOH-AL00; Android 10; Scale/3.00)',
    'Cookie': 'AI_YFD_U=200000094; ai_persistent=nut0jVMHkYF8/33obc5FU43M143f6RGafAh5XBQy6sLou//Cp2ge5zVw+UMk2T+QKbe+jFnJSJU/4kXtH3zdpC/DJ1k/WEegJ6svtTK9zx8=; ai_sess=N7vk1699uUQvPNMI/0t67/kfbdyP3I4zOdrGYzyl7lPpQxarRh+GGpM3qmaMw3wL; deviceid=200000094'
  }
  s = requests.session()
  res = s.request(url=url,method='post',data=payload,headers=headers)
  print(res.text)
  def get_cookies(self):
    # user_data = self.__class__.res.json()
    cookie = self.__class__.res.cookies
    return cookie


class login:
  url = "https://ape-api.yuanfudao.biz/accounts/android/login"
  params = "_productId=1911&_hostProductId=1911&platform=android29&version=1.6.0&av=5"
  payload = "phone=o%2F%2BVnJRhhftClvMFZheWAckwrXGyGCQuHGWeb6OpQ2BmoBQ968301OxfRm%2FgV%2FzTbjcP%2FngsjYTPqojnbegNDdlup3jnY%2FJsv9g%2FRR1JvfRo9tLp%2BX38%2Fimlaa%2BQrmW3MpsrqYObgNzUjaZ%2BKJLaW5%2F8KOnk1elrIBGRu2p0uTI%3D&verification=CtrMtdT%2B4qNnxO6kB59S%2FFeI0Lj9PhB9w%2FwU2oiHqji5Hld7SF6TawiZi7ysHz3DxAqkMSV0J7ZW8Mq7Q6YBao%2BZKDaYBzfZcBjeamVcwlvRrTjGOGouE1ruEB40IegdY%2BbVIj89Ss0RUE%2B16yb0Sz6f2tR4CWkah0lPwsh%2BkLc%3D&autoRegister=true"
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
  }
  cookies = devices().get_cookies()
  s = devices().s
  res = s.request(url=url,method='post',headers=headers,data=payload,params=params)

  def get_cookies(self):
    # user_data = self.__class__.res.json()
    # print(user_data)
    cookie = self.__class__.res.cookies
    return cookie


if __name__ == '__main__':
  # d = devices()
  # d.get_cookies()
  r = login()
  cookies = r.get_cookies()
  print(cookies)
  # cookid_dict={}
  # for key,value in cookies.items():
  #   cookid_dict[key]=value
  #   # print(key+':'+value)
  # print(cookid_dict)
  # print(login.res.json())

