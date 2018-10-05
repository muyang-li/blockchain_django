# coding:utf-8

import datetime as date
import hashlib

def create_new_block(request):
    previous_index = Block.objects.order_by('-index')[0]
    last_block = Block.objects.get(index=previous_index)

    new_block = Block(index = last_block.index +1)
    new_block.timestamp = date.datetime.now()
    new_block.data = request.GET['data']
    new_block.previous_hash = last_block.self_hash
    sha.update(str(temp_block.index).encode("utf8") + 
               str(temp_block.timestamp).encode("utf8") +
               str(temp_block.data).encode("utf8") + 
               str(temp_block.previous_hash).encode("utf8")
              )
    new_block.self_hash = sha.hexdigest()
    new_block.save()
    #此处应该返回一个成功页面html，todo
    return_message = "数据上链成功！存储区块号为：" + str(new_block.index)+"\n"
                    +"区块哈希为：" + str(new_block.self_hash)
    return HttpResponse(str(return_message))
