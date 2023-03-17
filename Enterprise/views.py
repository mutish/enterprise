from django.shortcuts import render,redirect
from Enterprise.forms import ShoesForm
from Enterprise.models import Shoes, Adminshoe
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
# Create your templates here.
def shoes(request):
    if request.method == 'POST':
        form = ShoesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ShoesForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    shoes = Shoes.objects.all()
    return render(request, 'show.html', {'shoes': shoes})

def edit(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'edit.html', {'shoes': shoes})

def update(request, id):
    shoes = Shoes.objects.get(id=id)
    form = ShoesForm(request.POST, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return redirect(request, 'edit.html', {'shoes': shoes})


def check_out(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'checkout.html', {'shoes': shoes})

def payment(request,id):
    shoes = Shoes.objects.get(id=id)
    if request.method == 'POST':
        amount = shoes.shoes_price
        phoneNumber = request.POST.get('phonenumber')
        if not phoneNumber or not phoneNumber.isdigit:
            return HttpResponse('invalid phone number')
        if not amount or not amount.isdigit:
            return HttpResponse('invalid price')
        cl = MpesaClient()
        phone_number = int(phoneNumber)
        amount = int(amount)
        account_reference = 'VIATU ENTERPRISES'
        transaction_desc = 'paying shoes'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, "checkout.html", {"shoes": shoes})

def diplay(request):
    adminshoes = Adminshoe.objects.all()
    return render(request, 'admindisplay.html', {'adminshoes': adminshoes})

def checkout(request, id):
    adminshoes = Adminshoe.objects.get(id=id)
    return render(request, "admincheckout.html", {"adminshoes": adminshoes})


def checkoutpay(request, id):
    adminshoes = Adminshoe.objects.get(id=id)
    if request.method == 'POST':
        amount = adminshoes.shoesprice
        phoneNumber = request.POST.get('contact')
        if not phoneNumber or not phoneNumber.isdigit:
            return HttpResponse('invalid phone number')
        if not amount or not amount.isdigit:
            return HttpResponse('invalid price')
        cl = MpesaClient()
        phone_number = int(phoneNumber)
        amount = int(amount)
        account_reference = 'SELL SHOES'
        transaction_desc = 'paying shoes'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, "admincheckout.html", {"shoes": shoes})



def destory(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('/show')



