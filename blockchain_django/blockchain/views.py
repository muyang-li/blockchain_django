# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
import datetime as date
import hashlib

from .models import Block

from .forms import TransactionForm, IndexQueryForm

from .generate_chain import create_new_block

sha = hashlib.sha256()

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def add_block(request):
#     return render(request, 'add_block.html')

def query_block(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IndexQueryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            index = form.cleaned_data['index']
            object_block = Block.objects.get(index = index)
            if object_block in Block.objects.all():
                return HttpResponseRedirect("/query_result/?index="+str(object_block.index))
            else:
                return HttpResponse("所查询的区块不存在！")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IndexQueryForm()

    return render(request, 'query_block.html', {'form': form})

def query_result(request):
    index = request.GET['index']
    info_dict = {}
    object_block = Block.objects.get(index = index)
    info_dict['self_hash'] = object_block.self_hash
    info_dict['index'] = object_block.index
    info_dict['timestamp'] = object_block.timestamp
    info_dict['data'] = object_block.data
    info_dict['previous_hash'] = object_block.previous_hash
    return render(request, 'query_result.html', {'info_dict': info_dict})

#提交交易数据的表单
def add_block(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TransactionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = form.cleaned_data['tx_data']
            message = create_new_block(data)
            if message == "区块链为空！请先创建创世区块！":
                return HttpResponse(message)
            else:
                return HttpResponseRedirect('/added_block/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransactionForm()

    return render(request, 'add_block.html', {'form': form})

#提交交易数据的表单
def added_block(request):
    info_dict = {}
    latest_block = Block.objects.order_by('-index')[0]
    info_dict['self_hash'] = latest_block.self_hash
    info_dict['index'] = latest_block.index
    info_dict['data'] = latest_block.data
    info_dict['previous_hash'] = latest_block.previous_hash
    return render(request, 'added_block.html', {'info_dict': info_dict})

#创世区块创建
def gene_block(request):
    if Block.objects.exists():
        return_message = "区块链非空！请勿重复创建创世区块！"
    else:
        new_block = Block(index = 0)
        new_block.timestamp = date.datetime.now()
        new_block.data = "This is the genesis block! 这是创世区块！"
        new_block.previous_hash = "0"*64
        sha.update(str(new_block.index).encode("utf8") + 
                str(new_block.timestamp).encode("utf8") +
                str(new_block.data).encode("utf8") + 
                str(new_block.previous_hash).encode("utf8")
                )
        new_block.self_hash = sha.hexdigest()
        new_block.save()
        #此处应该返回一个成功页面html，todo
        return_message = "创世区块建立成功！" + "\n" +"区块哈希为：" + str(new_block.self_hash)

    return HttpResponse(str(return_message))
