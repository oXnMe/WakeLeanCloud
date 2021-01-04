# -*- coding: utf-8 -*-

import os
import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    wxpush('未传入参数')
    sys.exit(1)
s = 0
u = []
for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print('[%s] %s唤醒状态: %s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), urls[i], req.status_code))
    if req.status_code != 200:
        s += 1
        u.append(urls[i])
if s > 0:
    wxpush('%s唤醒失败' % u)
    sys.exit(1)

def wxpush(content):
    sckey = os.getenv('CONFIG_SCKEY')
    url = 'https://sc.ftqq.com/' + sckey + '.send'
    data = {'text':'LeanCloud 唤醒失败！','desp':content}
    result = requests.post(url,data)
    print(result)
