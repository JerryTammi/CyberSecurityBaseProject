from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Question, UserSecurityQuestion 

def homePageView(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        question_id = request.POST.get('question')
        answer = request.POST.get('answer')

        if not username or not email or not password1 or not password2 or not question_id or not answer:
            print('All fields are required!')
            return redirect('register')
        if len(username) < 3 or len(email) < 3:
            print('Username is too short')
            return redirect('register')
        if password1 != password2:
            print('Passwords do not match!')
            return redirect('register')
        if len(password1) < 4:
            print('Password is too short')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            print('Username already exists!')
            return redirect('register')
        
        user = User.objects.create_user(username, email, password1)
        user.save()

        question = Question.objects.get(pk = question_id)
        user_sec_ques = UserSecurityQuestion(question = question, answer = answer, user = user)
        user_sec_ques.save()

        return redirect('login')
    else:
        questions = Question.objects.all()
        return render(request, 'register.html', {'questions':questions})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            print('All fields required!')
            return redirect('login')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Credentials did not match!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def forgotten(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            print('All fields required!')
            return redirect('forgotten')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username = username)
            userSecQues = UserSecurityQuestion.objects.get(user = user)
            question = userSecQues.question.question_text
            return render(request, 'recover.html', {'username':username, 'question':question})
        return redirect('forgotten')
    else:
        return render(request, 'forgottenpassword.html')

def recover(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        username = request.POST.get('username')
        if not answer or not username:
            return redirect('forgotten')
        user = User.objects.get(username = username)
        userSecQues = UserSecurityQuestion.objects.get(user = user)
        security_question_answer = userSecQues.answer    
        if answer == security_question_answer:
            return render(request, 'changepassword.html', {'username':username})
        else:
            return redirect('forgotten')
    return redirect('forgotten')

def change_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not password1 or not password2 or not username:
            print('Both fields required!')
            return redirect('change', {'username':username})
        if password1 != password2:
            print('Passwords do not match!')
            return redirect('change', username)
        user = User.objects.get(username = username)
        user.set_password(password1)
        user.save()
        return redirect('login')
    else:
        return redirect('home')
    