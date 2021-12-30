from django.db import models

from django.contrib.auth.models import User

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = 'ip address'
    time_of_login = 'now()'

# from accounts.views
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            print('All fields required!')
            return redirect('login')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            #############
            # Making a record of the user logging in
            new_log = Log(user = user, location = 'ip-address', time_of_login = 'now()')
            new_log.save()
            #############
            login(request, user)
            return redirect('home')
        else:
            print('Credentials did not match!')
            return redirect('login')
    else:
        return render(request, 'login.html')

# from market.views
@login_required
def create_ad(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        #############
        # checking for unwanted listings
        #############
        forbidden_items = []
        if name in forbidden_items:
            print('You cannot sell that here >:|')
            return redirect('home')
        #############
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