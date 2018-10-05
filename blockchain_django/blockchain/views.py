# coding:utf-8

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_block(request):
    return render(request, 'add_block.html')

def query_block(request):
    return render(request, 'query_block.html')

def gene_block(request):
    return render(request, 'gene_block.html')
