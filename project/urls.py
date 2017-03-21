"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testapp.views import *
from reg_proc.views import *
from  fetch_deal.views import *
import settings

urlpatterns = [
    url(r'^nearby_deals/',deal_input),
    url(r'^signup/',signup),
    url(r'^otp_check/',otp_check),
    url(r'^deal_fetch/',fetch_deal),
    #url(r'^media/','django.views.static.serve',{'document_root': '/home/nived/django/uploads/'}),
    url(r'^gcm/',customergcm),
    #url(r'^image/',image_fetch),
    url(r'^forgot_pass/',forgotpass),
    url(r'^pass_ver/',passverification),
    url(r'^pass_change/',passchange),
    url(r'^resend_otp/',resend_otp),
    url(r'^login/',login),
    url(r'^contact/',contacts),
    url(r'^notification/',notification),
    url(r'^voucher_id/',voucher),
    url(r'^feedback/',feedback),

]
