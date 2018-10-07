# coding:utf-8

import datetime as date
import hashlib

#根据区块号查询区块哈希
def get_block_hash(request):
    index = request.GET['index']
    return_block = Block.objects.get(index = index)
    return_message = return_block.self_hash
    return HttpResponse(str(return_message))

#根据区块号查询区块父哈希
def get_block_previous_hash(request):
    index = request.GET['index']
    return_block = Block.objects.get(index = index)
    return_message = return_block.previous_hash
    return HttpResponse(str(return_message))

#根据区块号查询区块生成时间戳
def get_block_previous_hash(request):
    index = request.GET['index']
    return_block = Block.objects.get(index = index)
    return_message = return_block.timestamp
    return HttpResponse(str(return_message))

#根据区块号查询区块所含数据(未处理)
def get_block_previous_hash(request):
    index = request.GET['index']
    return_block = Block.objects.get(index = index)
    return_message = return_block.data
    return HttpResponse(str(return_message))

#查询最新区块
# def get_latest_block_hash():
#     latest_block = Block.objects.order_by('-index')[0]
    