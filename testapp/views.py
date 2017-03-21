from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json,random,string
from models import *
from django.views.decorators.csrf import csrf_exempt 
from forms import *
from reg_proc.models import *
import requests


@csrf_exempt
def deal_input(request):
	if request.method=='POST':
		form=deals_in(request.POST)
		if form.is_valid():
			image=form.cleaned_data['image']
			deal_validity=form.cleaned_data['deal_validity']
			store_name=form.cleaned_data['store_name']
			store_address=form.cleaned_data['store_address']
			store_phone=form.cleaned_data['store_phone']
			deal_heading=form.cleaned_data['deal_heading']
			deal_description=form.cleaned_data['deal_description']
			deal_activate=form.cleaned_data['deal_activate']
			weightage=form.cleaned_data['weightage']
			store_latitude=form.cleaned_data['store_latitude']
			store_longitude=form.cleaned_data['store_longitude']
			store_location=form.cleaned_data['store_location']
			deal_category=form.cleaned_data['deal_category']
			deal_type=form.cleaned_data['deal_type']
			deal_id=''.join(random.choice(string.uppercase+string.digits) for i in range(10))
			dbobject=deals(image=image,deal_category=deal_category,deal_validity=deal_validity,
				deal_activate=deal_activate,deal_description=deal_description,deal_heading=deal_heading,
				deal_type=deal_type,deal_id=deal_id,store_location=store_location,store_longitude=store_longitude,
				store_latitude=store_latitude,store_name=store_name,store_address=store_address,weightage=weightage,
				store_phone=store_phone)
			dbobject.save()
			n={}
			n['result']=1
			return HttpResponse(json.dumps(n),content_type='applcation/json')
	else:
		n['result']=0
		return HttpResponse(json.dumps(n),content_type='applcation/json')

@csrf_exempt
def contacts(request):
	if request.method=='POST':
		form=contact(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			contact_details=form.cleaned_data['contacts']
			dbobject=contacts_db(mobile=mobile,contact_details=contact_details)
			dbobject.save()
			n={}
			n['result']=1
			return HttpResponse(json.dumps(n),content_type='applcation/json')

@csrf_exempt
def notification(request):
	if request.method=='POST':
		form=notif(request.POST)
		n={}
		if form.is_valid():
			heading=form.cleaned_data['heading']
			textz=form.cleaned_data['text']
			image=form.cleaned_data['image']
			
			#n['result']=textz
			#return HttpResponse(json.dumps(n),content_type='applcation/json')


			dbobject=notifications(textz=textz,image=image,heading=heading)
			dbobject.save()

			#dbobject=contacts_db(contact_details=image,mobile=9566276547)
			#dbobject.save()

			
			dbobject=signup_db.objects.all()
			

			k=0
			for i in dbobject:
				pson={'delay_while_idle': True, 'collapse_key': 'score_update', 'time_to_live': 108, 'data': {'text':textz,'heading':heading,'image':image},'registration_ids':[dbobject[k].gcmid]}
               
				h={'Content-Type': 'application/json', 'Authorization': 'key=AIzaSyBxEodHSh3moPoMwYkipLEXAhYUn3rptTg'}
				kson=json.dumps(pson)
				r=requests.post("https://android.googleapis.com/gcm/send",data=kson,headers=h)
			n={}
			n['result']=1
			return HttpResponse(json.dumps(n),content_type='applcation/json')

@csrf_exempt
def feedback(request):
	if request.method=='POST':
		form=feedbacks(request.POST)
		n={}
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			feeds=form.cleaned_data['feedback']
			dbobject=feed(feeds=feeds,mobile=mobile)
			dbobject.save()
			n={}
			n['result']=1
			return HttpResponse(json.dumps(n),content_type='applcation/json')
	else:
		n['result']=0
		return HttpResponse(json.dumps(n),content_type='applcation/json')
