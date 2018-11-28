"""blockchain_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blockchain import views as blockchain_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blockchain_views.home,name='home'),
    path('add_block/',blockchain_views.add_block,name='add_block'),
    path('added_block/',blockchain_views.added_block,name='added_block'),
    path('query_block/',blockchain_views.query_block,name='query_block'),
    path('query_result/',blockchain_views.query_result,name='query_result'),
    path('gene_block/',blockchain_views.gene_block,name='gene_block'),
    #添加真实数据后
    path('query_id/',blockchain_views.query_id,name='query_id'),#根据身份证号查询过包数据
    path('query_id_id/',blockchain_views.query_id_result,name='query_id_result'),#身份证号查询过包数据结果页面

]
