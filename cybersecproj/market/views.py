from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from market.models import Ad, Owner

@login_required
def create_ad(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        if not name or not price:
            print('All fields required!')
            return redirect('ad')
        seller = request.user
        new_add = Ad(name = name, price = price)
        new_add.save()
        owner = Owner(ad = new_add, owner = seller)
        owner.save()
        return redirect('home')
    else:
        return render(request, 'createad.html')

def list_ads(request):
    list = Owner.objects.all()
    return render(request, 'listads.html', {'list':list})

@login_required
@csrf_exempt
def buy(request):
    if request.method == 'GET':
        ad_id = request.GET.get('ad_id')
        ad = Ad.objects.get(id = ad_id)
        if ad.sold == True:
            return redirect('list_ads')
        buyer = request.user
        seller = Owner.objects.get(ad = ad)
        seller_id = seller.owner.id
        if buyer.id == seller_id:
            print('Cannot buy your own product!')
            return redirect('list_ads')
        seller.owner = buyer
        seller.save()
        ad.sold = True
        ad.save()
        return redirect('home')
    else:
        return redirect('home')


def personal_list(request, id):
    owner = User.objects.get(id = id)
    list = Owner.objects.filter(owner = owner)
    return render(request, 'listpersonal.html', {'list':list, 'username':owner.username})

