@login_required
def buy(request):
    if request.method == 'POST':
        ad_id = request.POST.get('ad_id')
        ad = Ad.objects.get(id = ad_id)
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