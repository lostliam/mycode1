import os,time,requests,random,json

alldata=json.loads(os.getenv('LYMG'))


import smtplib
from email.mime.text import MIMEText
def testsentemail(title):
    host = alldata['host']
    port = 465
    sender = alldata['sender']
    pwd = alldata['pwd']
    receiver = alldata['receiver']
    body = '<h1>磁盘碎片已整理</h1>'
    msg = MIMEText(body, 'html')
    msg['subject'] = title
    msg['from'] = sender
    msg['to'] = receiver
    try:
        s = smtplib.SMTP_SSL(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())
        print('Done.sent email success')
    except smtplib.SMTPException:
        print('Error.sent email fail')

def slogin():
    try:
        HEADERS={'Connection': 'keep-alive', 'Content-Length': '200', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"', 'Accept': '*/*', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56', 'sec-ch-ua-platform': '"Windows"', 'Origin':alldata['origin'], 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': alldata['refer'], 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        print(HEADERS)
        r = requests.post(url=alldata['url'], data=alldata['data'], timeout=5,headers=HEADERS, verify=False,)
        # print(r.text)
        a=json.loads(r.text)
        print(a['msg'])
        testsentemail(str(random.randint(1,100))+str(random.randint(1,100))+a['msg']+str(random.randint(1,100))+str(random.randint(1,100)))
    except:
        time.sleep(10)
        slogin()

number=random.randint(1,100)
print(number)
slogin()
if number>100:
    slogin()

