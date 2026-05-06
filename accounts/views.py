from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm
from .models import MagicLinkToken
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def registo_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login_view')

    return render(request, 'accounts/registo.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user:
            auth_login(request, user)
            return redirect('portfolio_home')
        else:
            return render(request, 'accounts/login.html', {'mensagem': 'Credenciais inválidas'})

    return render(request, 'accounts/login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('portfolio_home')


def magic_link_request_view(request):
    mensagem = None
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        # Always show the same message to avoid leaking which emails exist
        mensagem = 'Se o email existir na nossa base de dados, irás receber um link de acesso.'
        try:
            user = User.objects.get(email=email)
            token_obj = MagicLinkToken.objects.create(user=user)
            link = request.build_absolute_uri(f'/accounts/magic/{token_obj.token}/')
            send_mail(
                subject='O teu link de acesso',
                message=f'Clica no link para entrares:\n\n{link}\n\nExpira em 15 minutos.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
        except User.DoesNotExist:
            pass

    return render(request, 'accounts/magic_link_request.html', {'mensagem': mensagem})


def magic_link_verify_view(request, token):
    token_obj = get_object_or_404(MagicLinkToken, token=token)
    if not token_obj.is_valid():
        return render(request, 'accounts/magic_link_invalid.html')

    token_obj.used = True
    token_obj.save()
    auth_login(request, token_obj.user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('portfolio_home')
