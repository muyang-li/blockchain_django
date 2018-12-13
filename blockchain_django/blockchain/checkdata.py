import datetime as date
import hashlib
import requests 

from .models import Block,CommonUser
from blockchain.generate_chain import create_new_block, create_gene_block

sha = hashlib.sha256()

#先只做4号安检机
def check_new_data():
    if (Block.objects.all().count() == 0):
        create_gene_block()
    last_block = Block.objects.last()#最新区块
    last_time = last_block.dpCreationTime#以过包时间作为拉去新数据的标准。
    last_time_str = datetime_to_iso8601(str(last_time))#最新时间的正常格式，字符串
    get_url = "http://112.65.156.58:9000/v2/odata/datapoints?$filter=DeviceNumber eq '000000004' "+"and dpCreationTime gt "+last_time_str+"&$orderby=dpCreationTime desc"

    r = requests.get(get_url)
    rjson = r.json()
    rlist = rjson['value']#包含着所有过包信息的列表，列表元素为字典，每个字典代表一个过包记录？

    #遍历整个列表，生成区块

    outputlist = []
    for record in rlist:
        trackNum = str(record['ID'])
        deviceId = str(record['DeviceId'])
        deviceName = str(record['DeviceName'])
        dpCreationTime = date.datetime.strptime(iso8601ToNormal(str(record['DpCreationTime'])),'%Y-%m-%dT%H:%M:%S')
        location = str(record['StrValue4'])
        image = str(record['StrValue1'])
        create_new_block(trackNum,deviceId,deviceName,dpCreationTime,location,image)
        outputlist.append('数据'+trackNum+'成功上链！')
    return_message = '执行完毕！'+str(outputlist)
    return return_message



def datetime_to_iso8601(timestr): #将数据库存储的datetime对象转化为http请求中需要的格式，参数为字符串
    timelist = list(timestr)
    return_time = "".join(timelist[:10]) + "T" + "".join(timelist[11:19]) + "%2B08:00"
    return return_time

def iso8601ToNormal(isostr):#iso8601格式的时间，转换成正常的时间格式，返回字符串
    timelist = list(isostr)
    dotindex = timelist.index('.')
    normalstr = "".join(timelist[:dotindex])
    return normalstr