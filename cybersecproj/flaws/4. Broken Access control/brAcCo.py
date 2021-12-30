from django.shortcuts import redirect
from market.models import Owner

# from market.models
@login_required
def delete(request):
    if request.method == 'POST':
        ad_id = request.POST.get('ad_id')
        ad = Ad.objects.get(id = ad_id)
        if ad.sold == True:
            return redirect('list_ads')
        #############
        # Checking if credentials match
        owner = Owner.objects.get(ad = ad)
        if user.id != owner.owner.id:
            print('Not your ad to delete!')
            return redirect('home')
        #############
        ad.deleted = True
        ad.save()
        return redirect('home')
    else:
        return redirect('home')