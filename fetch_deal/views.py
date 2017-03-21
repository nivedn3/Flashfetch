from django.shortcuts import render
from models import *
from  reg_proc.models  import *
from testapp.models  import *
from django.views.decorators.csrf import csrf_exempt 
from forms import *
from django.http import HttpResponse
import json,random,string

# Create your views here.

@csrf_exempt
def fetch_deal(request):
	if request.method=='POST':
		form=fetch(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			token=form.cleaned_data['token']
			try:
				p=signup_db.objects.get(mobile=mobile,token=token)
				k=1
			except:
				k=0
			j={}
			if  k:
				p=0
				n={}
				r=[]
				dbobject=deals.objects.all().order_by('weightage')				
				for i  in dbobject:
					n['deal_validity']=str(dbobject[p].deal_validity)
					n['deal_category']=dbobject[p].deal_category
					n['deal_type']=dbobject[p].deal_type
					n['store_name']=dbobject[p].store_name
					n['store_location']=dbobject[p].store_location
					n['store_address']=dbobject[p].store_address
					ph=str(dbobject[p].store_phone)
					phl=list(ph)
					if phl[0]=='*':
						phl[0]='0'
					ph=''.join(phl)
					n['store_phone']=ph
					n['store_latitude']=dbobject[p].store_latitude
					n['store_longitude']=dbobject[p].store_longitude
					n['deal_heading']=dbobject[p].deal_heading
					s=str(dbobject[p].deal_description)
					ls=list(s)
					k=0
					for i in ls:
						if i=='*':
							ls[k]='\n'
						k=k+1

					n['deal_description']=''.join(ls)
					s=str(dbobject[p].deal_activate)
					ls=list(s)
					k=0
					for i in ls:
						if i=='*':
							ls[k]='\n'
						k=k+1

					n['deal_activate']=''.join(ls)
					n['weightage']=dbobject[p].weightage
					n['deal_id']=dbobject[p].deal_id
					n['image']=dbobject[p].image
					n['activated']=dbobject[p].activate

					try:
						dbobject1=vouchers_db.objects.get(deal_id=dbobject[p].deal_id,mobile=mobile)
						n['voucher_id']=str(dbobject1.voucher_id)
						act=1
					except:
						act=0
					
					n['activatedre']=act

					r.append(n)
					n={}
					p=p+1									
				j['result']=1
				j['deals']=r
				return HttpResponse(json.dumps(j),content_type='application/json')
			else:
				j['result']=0
				return HttpResponse(json.dumps(j),content_type='application/json')


#@csrf_exempt
#def image_fetch(request):
#	if request.method=='POST':
#		path=request.POST.get('path','')
#		image=open('%s'%path,'rb')
#		response = HttpResponse(content=image)
#		response['Content-Type'] = 'image'
#		response['Content-Disposition'] = 'attachment; filename="%s.png"' \
#                                 % 'test'
#		return response

@csrf_exempt
def voucher(request):
	if request.method=='POST':
		form=voucher_form(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			token=form.cleaned_data['token']
			deal_id=form.cleaned_data['deal_id']
			try:
				p=signup_db.objects.get(mobile=mobile,token=token)
				k=1
			except:
				k=0
			n={}
			if k:
				test=vouchers_db.objects.filter(mobile=mobile,deal_id=deal_id)
				if test:
					voucher_id=test[0].voucher_id
				else:
					voucher_id=''.join(random.choice(string.uppercase+string.digits) for i in range(6))
					dbobject1=deals.objects.get(deal_id=deal_id)
					
					dbobject1.save()
					dbobject=vouchers_db(mobile=mobile,deal_id=deal_id,voucher_id=voucher_id,activate=1)
					dbobject.save()					
				n['result']=1
				n['voucher_id']=voucher_id
				return HttpResponse(json.dumps(n),content_type='application/json')
			else:
				n['result']=0
				return HttpResponse(json.dumps(n),content_type='application/json')
