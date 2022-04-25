#加载模块

import requests

import re

import json

import csv

import pandas as pd

#身份伪装，其实没必要

headers={

        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'

        }

#请求地址

url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'

#发送请求

response=requests.get(url=url,headers=headers)

#数据解析

data_html=response.text

#【0】转换数据类型从list到str,强大的正则

json_str=re.findall('"component":\[(.*)\],',data_html)[0]

#转换字典

json_dict=json.loads(json_str)

caseList=json_dict['caseList']

for case in caseList:

    area=case['area']#

    confirmed=case['confirmed']#

    curConfirm=case['curConfirm']

    asymptomatic=case['asymptomatic']

    crued=case['crued']#

    died=case['died']#

    confirmedRelative=case['confirmedRelative']

    diedRelative=case['diedRelative']

    curedRelative=case['curedRelative']

    asymptomaticRelative=case['asymptomaticRelative']

    nativeRelative=case['nativeRelative']

    overseasInputRelative=case['overseasInputRelative']

    print(area,confirmed,curConfirm,confirmedRelative,nativeRelative,overseasInputRelative, asymptomatic,asymptomaticRelative,crued,curedRelative,died,diedRelative)

    with open('./data2.csv', mode='a', encoding='utf-8', newline='')as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(
            [area, confirmed, curConfirm, confirmedRelative, nativeRelative, overseasInputRelative, asymptomatic,
             asymptomaticRelative, crued, curedRelative, died, diedRelative])
#写入表格

