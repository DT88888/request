import requests
res=requests.get("http://www.doit.am/") #GET请求
res=requests.post("http://www.doit.am/") #POST请求
res=requests.put("http://www.doit.am/") #PUT请求
res=requests.delete("http://www.doit.am/") #DELETE请求
res=requests.head("http://www.doit.am/") #HEAD请求
res=requests.options("http://www.doit.am/") #OPTIONS请求

print(res.apparent_encoding) #编码方式
print(res.content) #返回响应的内容，以字节为单位
print(res.cookies) #返回一个 CookieJar 对象，包含了从服务器发回的 cookie
print(res.elapsed) #返回一个 timedelta 对象，包含了从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如 r.elapsed.microseconds 表示响应到达需要多少微秒。
print(res.encoding) #解码 r.text 的编码方式
print(res.headers) #返回响应头，字典格式
print(res.history) #返回包含请求历史的响应对象列表（url）
print(res.is_permanent_redirect) #如果响应是永久重定向的 url，则返回 True，否则返回 False
print(res.is_redirect) #如果响应被重定向，则返回 True，否则返回 False
print(res.links) #返回响应的解析头链接
print(res.next)	#返回重定向链中下一个请求的 PreparedRequest 对象
print(res.ok) #检查 "status_code" 的值，如果小于400，则返回 True，如果不小于 400，则返回 False
print(res.reason) #响应状态的描述，比如 "Not Found" 或 "OK"
print(res.request) #返回请求此响应的请求对象
print(res.status_code) #返回 http 的状态码，比如 404 和 200（200 是 OK，404 是 Not Found）
print(res.text)	#返回响应的内容，unicode 类型数据
print(res.url) #返回响应的 URL