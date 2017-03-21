from django.shortcuts import render
from reg_proc.forms import *
from models import *
from random import randint
import random,string
from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt 



# Create your views here.

@csrf_exempt
def signup(request):
	if request.method=='POST':
		form=signup_form(request.POST)
	
		if form.is_valid():
			
			name=form.cleaned_data['name']
			mobile=form.cleaned_data['mobile']
			password=form.cleaned_data['password']
			referral=form.cleaned_data['referral']
			email=form.cleaned_data['email']

			try:
				dbobject=signup_db.objects.get(mobile=mobile)
				k=0
			except:
				k=1
			n={}
			if k:
				token=''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(32))
				#concern as this should be a primary key 
				referral_id=''.join(random.choice(string.uppercase+string.digits) for i in range(6))
				profile_id=''.join(random.choice(string.uppercase+string.digits) for i in range(6))
				otp=randint(100000,999999)
				dbobject=signup_db(name=name,mobile=mobile,email=email,token=token,referral=referral,password=password,
					referral_id=referral_id,otp=otp,profile_id=profile_id)
				dbobject.save()
				try:
					dbobject1=signup_db.objects.get(referral_id=referral)
					ref=1
				except:
					ref=0

				if ref:
					dbobject1.no_of_refs=dbobject1.no_of_refs+1
					n['referral']=1
				else:
					n['referral']=0

				try:
					t=requests.get('http://bhashsms.com/api/sendmsg.php?user=8754556606&pass=984b5ac&sender=FFETCH&phone=%d&text=Hi %s , Thank you for signing up with FlashFetch. Great deals are waiting for you on the other side. Join us with this OTP %d&priority=ndnd&stype=normal'%(mobile,name,otp))
					eflag=1
				except:
					eflag=0
				
				n['result']=1
				n['token']=token
				n['eflag']=eflag
				n['referral_id']=referral_id	
				n['profile_id']=profile_id			
				return HttpResponse(json.dumps(n),content_type='application/json')
			else:
				#already exists
				n={}
				n['result']=-1
				return HttpResponse(json.dumps(n),content_type='application/json')

@csrf_exempt
def otp_check(request):
	if request.method=='POST':
		form=otp(request.POST)
		if form.is_valid():
			otp_in=form.cleaned_data['otp_in']
			mobile=form.cleaned_data['mobile']
			token=form.cleaned_data['token']
			try:
				dbobject=signup_db.objects.get(mobile=mobile,otp=otp_in,token=token)
				k=1
			except:
				k=0
			n={}
			if k:				
				n['result']=1
				dbobject.otp_ver=1
				dbobject.save()
				return HttpResponse(json.dumps(n),content_type='application/json')
			else:
				n['result']=0
				return HttpResponse(json.dumps(n),content_type='application/json')

@csrf_exempt
def customergcm(request):
	if request.method=='POST':
		form=cusgcm(request.POST)
		if form.is_valid():			
			gcmid=form.cleaned_data['gcmid']
			token=form.cleaned_data['token']
			mobile=form.cleaned_data['mobile']
			try:
				dbobject=signup_db.objects.get(token=token,mobile=mobile)
				k=1
			except:
				k=0
			n={}
			if k:
				dbobject.gcmid=gcmid
				dbobject.save()
				n['result']=1
				return HttpResponse(json.dumps(n), content_type='application/json' )			
			elif k==0:
				n['result']=0
				return HttpResponse(json.dumps(n), content_type='application/json' )


@csrf_exempt
def login(request):
	if request.method=='POST':
		form=log(request.POST)
		if form.is_valid():
			password=form.cleaned_data['password']
			mobile=form.cleaned_data['mobile']
			try:
				dbobject=signup_db.objects.get(password=password,mobile=mobile)
				k=1
			except:
				k=0
			n={}
			if k:
				token=''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(32))
				dbobject.token=token
				dbobject.save()

				n['result']=1
				n['token']=token
				n['otp_ver']=dbobject.otp_ver
				n['name']=dbobject.name
				n['email']=dbobject.email
				n['referral']=dbobject.referral
				n['referral_id']=dbobject.referral_id
				return HttpResponse(json.dumps(n),content_type='application/json')
			else:
				n['result']=0
				return HttpResponse(json.dumps(n),content_type='application/json')


@csrf_exempt
def resend_otp(request):
	if request.method=='POST':
		form=rotp(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			token=form.cleaned_data['token']
			try:
				dbobject=signup_db.objects.get(mobile=mobile,token=token)
				k=1
			except:
				k=0
			n={}
			if k:
				otp=dbobject.otp
				name=dbobject.name
				try:
					t=requests.get('http://bhashsms.com/api/sendmsg.php?user=8754556606&pass=984b5ac&sender=FFETCH&phone=%d&text=Hi %s , Thank you for signing up with FlashFetch. Great deals are waiting for you on the other side. Join us with this OTP %d&priority=ndnd&stype=normal'%(mobile,name,otp))
					eflag=1
				except:
					eflag=0
				n['result']=1
				n['eflag']=eflag
				return HttpResponse(json.dumps(n),content_type='application/json')
			else:
				n['result']=0
				return HttpResponse(json.dumps(n),content_type='application/json')


@csrf_exempt
def forgotpass(request):
	if request.method=='POST':
		#mobile=request.POST.get('mobile','')
		form=fpassword(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			try:
				dbobject=signup_db.objects.get(mobile=mobile)
				k=1
			except:			
				k=0
			n={}
			if k:
				fpass=randint(99999,999999)
				name=dbobject.name
				dbobject.fpass=fpass
				dbobject.save()
				try:
					t=requests.get('http://bhashsms.com/api/sendmsg.php?user=8754556606&pass=984b5ac&sender=FFETCH&phone=%d&text=Hi %s , OTP for changing your password is %d&priority=ndnd&stype=normal'%(mobile,name,fpass))
					eflag=1
				except:
					eflag=0
				n['result']=1
				n['eflag']=eflag
				return HttpResponse(json.dumps(n), content_type='application/json' )
			elif k==0:
				n['result']=0
				return HttpResponse(json.dumps(n), content_type='application/json' )

@csrf_exempt
def passverification(request):
	if request.method=='POST':
		#mobile=request.POST.get('mobile','')
		#verif=request.POST.get('verif','')
		form=pver(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			verif=form.cleaned_data['verif']
			try:
				dbobject=signup_db.objects.get(mobile=mobile)
				k=1
			except:			
				k=0
			n={}
			if k:
				if verif==dbobject.fpass:
					n['result']=1
					return HttpResponse(json.dumps(n), content_type='application/json' )
				else:
					n['result']=0
					return HttpResponse(json.dumps(n), content_type='application/json' )
			elif  k==0:
				n['result']=-1
				j_d=json.dumps(n)				
				return HttpResponse(json.dumps(n), content_type='application/json' )

@csrf_exempt
def passchange(request):
	if request.method=='POST':
		#mobile=request.POST.get('mobile','')
		#npass=request.POST.get('npass','')
		form=cpass(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			npass=form.cleaned_data['npass']
			try:
				dbobject=signup_db.objects.get(mobile=mobile)
				k=1
			except:
				k=0
			n={}
			if k:
				dbobject.password=npass
				dbobject.save()
				n['result']=1
				return HttpResponse(json.dumps(n), content_type='application/json' )
			else:
				n['result']=0
								
				return HttpResponse(json.dumps(n), content_type='application/json' )
