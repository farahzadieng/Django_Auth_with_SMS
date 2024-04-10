from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login

from .forms import SignUpForm

import random 
from .api_sms import send_verification_code


User = get_user_model()
    
def signup_page_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            if not User.objects.filter(phone_number=phone_number).exists():
                verification_code = str(random.randint(100000, 999999))
                send_verification_code(phone_number, verification_code)
                request.session['verification_code'] = verification_code
                request.session['phone_number'] = phone_number
                return redirect('verify_signup')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def verify_signup_view(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        session_code = request.session.get('verification_code')
        session_phone = request.session.get('phone_number')
        if verification_code == session_code:
            user = User.objects.create_user(phone_number=session_phone)
            user.save()
            del request.session['verification_code']
            del request.session['phone_number']
            return redirect('signup')
        else:
            message = 'Code not Valid! Please retry. '
            return render(request, 'users/signup_verify.html', {'message': message})
    return render(request, 'users/signup_verify.html')


def login_page_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if len(phone_number) < 11 or phone_number[0:2] != '09':
            message = '''
                    * Please provide a valid phone number !
                    * Phone numbers must start with 09
                    '''
            return render(request, 'users/login.html', {'message': message})
        else:
            if User.objects.filter(phone_number=phone_number).exists():
                verification_code = str(random.randint(100000, 999999))
                send_verification_code(phone_number, verification_code)
                request.session['phone_number'] = phone_number
                request.session['verification_code'] = verification_code
                return redirect('verify_login')
            else:
                message = 'Phone Number is not registered on the website ! '
                return render(request, 'users/login.html', {'message':message})
    return render(request, 'users/login.html')


def verify_login_view(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        if verification_code == request.session['verification_code']:
            user = User.objects.get(phone_number=request.session['phone_number'])
            del request.session['verification_code']
            del request.session['phone_number']
            login(request, user)
            return redirect('signup')
        else:
            message = 'Code not Valid! Please retry. '
            return render(request, 'users/login_verify.html', {'message': message})
    return render(request, 'users/login_verify.html')

