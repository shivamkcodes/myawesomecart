from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from.models import Product,Contact,Orders,OrderUpdate
import json
from django.views.decorators.csrf import csrf_exempt

#from PayTm import Checksum
#import Checksum
#import base64
#MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'
def index(request):
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1,nSlides),nSlides])
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)


def search(request):
    query=request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchmatch(query,item)]
        n = len(prodtemp)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
         allprods.append([prodtemp, range(1, nSlides), nSlides])
    params = {'allprods': allprods, "msg": ""}
    if len(allprods) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def searchmatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
  #  if query in item.desc or query in item.product_name or query in item.category :

        return True
    else:
        return False


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        query=request.POST.get('query','')
        contact=Contact(contact_name=name,email=email,phone=phone,query=query)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({ "status": "success","updates": updates, "itemJson":order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{ "status": "noitem"}')
        except Exception as e:
            return HttpResponse('{ "status": "error"}')

    return render(request, 'shop/tracker.html')



def productView(request,myid):
    #fetching the product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/productview.html',{'product':product[0]})


def checkout(request):
    if request.method == "POST":
        items_json=request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders(items_json=items_json,name=name, email=email, phone=phone,address=address,state=state,city=city,zip_code=zip_code ,amount=amount)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="the order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})

        #request paytm to transfer the account to your bank after payment by user

        # params_dict={
        #
        #     'MID': 'WorldP64425807474247',
        #     'ORDER_ID': order.order_id,
        #     'TXN_AMOUNT': str(amount),
        #     'CUST_ID': email,
        #     'INDUSTRY_TYPE_ID': 'Retail',
        #     'WEBSITE': 'webstaging',
        #     'CHANNEL_ID': 'WEB',
        #     'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        #
        # }
        # params_dict['CHECKSUMHASH'] = Checksum.generate_checksum(params_dict, MERCHANT_KEY)
        # params_dict['CHECKSUMHASH']=Checksum.generate_checksum(params_dict,MERCHANT_KEY)
        #return render(request,'shop/paytm.html',{'param_dict':params_dict})
    return render(request,'shop/checkout.html')

#paytm will send request here
# @csrf_exempt
# def handlerequest(request):
#     return HttpResponse("shivam")


