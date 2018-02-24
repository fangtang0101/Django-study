# -*- coding: utf-8 -*-

from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'^$', view.hello),
    # url(r'^hello$', view.hello), 若用此处的代码，请注释上面的代码，正则陪陪 url，然后返回 展示的页面
]
