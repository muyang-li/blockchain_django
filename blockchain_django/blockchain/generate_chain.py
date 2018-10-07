# coding:utf-8

import datetime as date
import hashlib
from .models import Block

sha = hashlib.sha256()


# def create_new_block(request):
#     if Block.objects.exists():
#         previous_index = Block.objects.order_by('-index')[0]
#         last_block = Block.objects.get(index=previous_index)

#         new_block = Block(index = last_block.index +1)
#         new_block.timestamp = date.datetime.now()
#         new_block.data = request.GET['data']
#         new_block.previous_hash = last_block.self_hash
#         sha.update(str(temp_block.index).encode("utf8") + 
#                 str(temp_block.timestamp).encode("utf8") +
#                 str(temp_block.data).encode("utf8") + 
#                 str(temp_block.previous_hash).encode("utf8")
#                 )
#         new_block.self_hash = sha.hexdigest()
#         new_block.save()
#         #此处应该返回一个成功页面html，todo
#         return_message = "数据上链成功！存储区块号为：" + str(new_block.index)+"\n"
#                         +"区块哈希为：" + str(new_block.self_hash)
#     else:
#         return_message = "区块链为空！请先创建创世区块！"

#     return HttpResponse(str(return_message))

def create_new_block(tx_data):
    if Block.objects.exists():
        last_block = Block.objects.order_by('-index')[0]

        new_block = Block(index = last_block.index +1)
        new_block.timestamp = date.datetime.now()
        new_block.data = tx_data
        new_block.previous_hash = last_block.self_hash
        sha.update(str(new_block.index).encode("utf8") + 
                str(new_block.timestamp).encode("utf8") +
                str(new_block.data).encode("utf8") + 
                str(new_block.previous_hash).encode("utf8")
                )
        new_block.self_hash = sha.hexdigest()
        new_block.save()
        #此处应该返回一个成功页面html，todo
        return_message = "数据上链成功！存储区块号为：" + str(new_block.index)+"\n" +"区块哈希为：" + str(new_block.self_hash)
    else:
        return_message = "区块链为空！请先创建创世区块！"

    return return_message

#创世区块创建
def create_gene_block(request):
    if Block.objects.exists():
        return_message = "区块链非空！请勿重复创建创世区块！"
    else:
        new_block = Block(index = 0)
        new_block.timestamp = date.datetime.now()
        new_block.data = "This is the genesis block! 这是创世区块！"
        new_block.previous_hash = "0"*64
        sha.update(str(temp_block.index).encode("utf8") + 
                str(temp_block.timestamp).encode("utf8") +
                str(temp_block.data).encode("utf8") + 
                str(temp_block.previous_hash).encode("utf8")
                )
        new_block.self_hash = sha.hexdigest()
        new_block.save()
        #此处应该返回一个成功页面html，todo
        return_message = "创世区块建立成功！" + "\n" +"区块哈希为：" + str(new_block.self_hash)

    return HttpResponse(str(return_message))
