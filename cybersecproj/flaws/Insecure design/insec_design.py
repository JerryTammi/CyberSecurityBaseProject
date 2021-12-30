from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

#code pulled from accounts.views
def forgotten(request):
    if request.method == 'POST':
        email_address = request.POST.get('email_address')
        if not email_address:
            print('All fields required!')
            return redirect('forgotten')
        if User.objects.filter(email=email_address).exists():
            # Obviously this does not work at the moment, it would require more functionality 
            # which includes sender_email, verifying the users email during
            # registration, and a proper function for redirecting to changepassword.html.
            subject = 'CyberSecProj Password Recovery'
            message = 'redirect to changepassword.html'
            sender = 'cybersecproj@email.com'
            to = email_address
            send_mail(
                subject,
                message, 
                sender, 
                [to], 
                fail_silently=False,
                )
            print('Recovery email has been sent')
            return render(request, 'recoveryemailsent.html')
        return redirect('forgotten')
    else:
        return render(request, 'forgottenpassword.html')